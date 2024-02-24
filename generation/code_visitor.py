import ast
from copy import copy
from itertools import permutations

from config import final_answer_name
from problem_solving_tree import *


class NumberCounter(ast.NodeVisitor):
    def __init__(self):
        self.numbers = []

    def visit_Constant(self, node):
        if isinstance(node.value, int) or isinstance(node.value, float):
            self.numbers.append(node.value)


class ProbSolveTreeVisitor(ast.NodeVisitor):
    def __init__(self, original_question, original_answer):
        nums_in_question, question_string = util.get_all_num_from_string(original_question)
        self.nums_in_question = nums_in_question
        # Corresponding node to the number
        self.assign_node = [None] * len(nums_in_question)
        self.versions = None
        # Dict of ast.Assign that can be changed both in the question and the code
        self.changeable_variables = {}
        # Constant nodes
        self.constants = {}
        # Dict of all ast Nodes, used to check if a Name has already been assigned
        self.all_nodes = {}
        # Nodes with the same numbers for number misalignment
        self.same_num_nodes = {}
        # Formatted question string
        self.formatted_question = question_string

        self.original_answer = original_answer
        self.original_question = original_question

        # Stats of generation
        self.determined_value_type = False
        self.maximum_generate_times = 0
        self.sum_generate_times = 0
        self.total_generate_times = 0

        self.temp_varname_gen = util.generate_temp_name("var")
        self.temp_const_name_gen = util.generate_temp_name("const")

    def get_new_instance(self, requirement):
        # Get the answer node (root)
        final_node: BaseNode = self.all_nodes[final_answer_name]

        # Determine properties of the nodes
        if not self.determined_value_type:
            final_node.determine_value_type()
            self.determined_value_type = True

        # Start generating values
        final_node.generate_values(requirement)
        final_node.simplify()
        value_type = final_node.get_value_type()
        self.total_generate_times += 1

        # Return the new list of numbers that should be added to the problem
        res = [None] * len(self.assign_node)
        for i, node in zip(self.versions[0], self.assign_node):
            if node:
                res[i] = node.get_gen_val()
            else:
                res[i] = self.nums_in_question[i]
        return res, value_type

    def generate_versions(self):
        # Get the answer node (root)
        final_node: BaseNode = self.all_nodes[final_answer_name]

        # Determine properties of the nodes
        if not self.determined_value_type:
            final_node.determine_value_type()
            self.determined_value_type = True

        # Start generating values
        final_node.generate_values('M1')
        final_node.simplify()

        versions = [list(range(len(self.assign_node)))]
        for val, node_indices in self.same_num_nodes.items():
            new_versions = []
            perm = permutations(node_indices)
            for p in list(perm):
                for version in versions:
                    new_version = copy(version)
                    for old, new in zip(node_indices, p):
                        new_version[new] = version[old]
                    new_versions.append(new_version)
            versions = new_versions

        self.versions = versions

    def merge_versions(self):
        final_node: BaseNode = self.all_nodes[final_answer_name]
        answer = final_node.get_val()
        versions = self.versions
        answers = []

        old_one_vals = [node.get_val() if node is not None else None for node in self.assign_node]
        for version in versions:
            # Check if answer is the same
            for index, old_index in zip(version, range(len(self.assign_node))):
                if index != old_index:
                    self.assign_node[index].set_val(old_one_vals[old_index])

            answers.append(final_node.get_val())

        # There is always one saved version
        saved_versions = [list(range(len(self.assign_node)))]
        saved_answers = {answer}
        for version, answer in zip(versions, answers):
            if answer not in saved_answers:
                saved_versions.append(version)
                saved_answers.add(answer)

        # Change the values back
        for i, node in enumerate(self.assign_node):
            if node is not None:
                node.set_val(old_one_vals[i])
        self.versions = saved_versions

    def produce_distinguishing_question(self):
        # Get the answer node (root)
        final_node: BaseNode = self.all_nodes[final_answer_name]

        # Start generating values
        all_unique = False

        answers = []
        old_one_vals = []
        while not all_unique:
            final_node.generate_values('M3')
            final_node.simplify()
            old_one_vals = [node.get_val() if node is not None else None for node in self.assign_node]
            all_unique = True
            answers = []
            for version in self.versions:
                for index, old_index in zip(version, range(len(self.assign_node))):
                    if index != old_index:
                        self.assign_node[index].set_val(old_one_vals[old_index])
                answer = final_node.get_val()
                if answer in answers:
                    all_unique = False
                    break
                answers.append(answer)

        nums = [old_one_vals[i] if old_one_vals[i] is not None else self.nums_in_question[i] for i in range(len(
            self.assign_node
        ))]

        return self.formatted_question.format(*nums), answers

    def visit_Assign(self, node):
        _id = node.targets[0].id
        if isinstance(node.value, ast.Constant):
            self.get_num_node(node.value, _id)
        # The binary operation might be nested, so we will send it to a recursive function
        else:
            new_node = self.parse_node(node.value)
            self.add_to_dict(_id, new_node, self.all_nodes, True)

    def visit_While(self, node):
        raise NotImplementedError("Has while")

    def visit_For(self, node):
        raise NotImplementedError("Has for")

    def visit_If(self, node):
        raise NotImplementedError("Has if")

    def visit_AugAssign(self, node):
        # Go inside the binary operation first
        left = self.parse_node(node.target)
        right = self.parse_node(node.value)
        # Create the BinOp Node
        res = BinOpNode(self.get_binop(node.op), [left, right])
        self.add_to_dict(node.target.id, res, self.all_nodes, True)

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call) and node.value.func.id == 'print':
            # This is the final answer
            answer_node = self.get_final_ans(node.value)

            if answer_node is None or not util.is_same_num(answer_node.get_val(), self.original_answer):
                raise NotImplementedError("Wrong answer")
            self.add_to_dict(final_answer_name, answer_node, self.all_nodes, True)

    def parse_node(self, ast_node):
        if isinstance(ast_node, ast.Name):
            return self.get_var_node(ast_node)
        elif isinstance(ast_node, ast.BinOp):
            return self.get_binop_node(ast_node)
        elif isinstance(ast_node, ast.UnaryOp):
            return self.get_unary_node(ast_node)
        elif isinstance(ast_node, ast.Constant):
            return self.get_num_node(ast_node)
        elif isinstance(ast_node, ast.Call):
            return self.get_call_node(ast_node)
        elif isinstance(ast_node, ast.JoinedStr):
            return self.get_str_node(ast_node)
        elif isinstance(ast_node, ast.Compare):
            raise NotImplementedError('Node Operation Compare')
        elif isinstance(ast_node, ast.IfExp):
            raise NotImplementedError('Has if')
        raise NotImplementedError(f"node operation has not being implemented: \n{ast.dump(ast_node, indent=4)}")

    def get_var_node(self, node):
        if node.id in self.all_nodes:
            return self.all_nodes[node.id]
        else:
            print(node.id)
            for k, v in self.all_nodes.items():
                print(f'{k}: {v}')
            raise NotImplementedError("The called node has not been assigned")

    def get_call_node(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = f'{node.func.value.id}.{node.func.attr}'
        else:
            raise NotImplementedError(ast.dump(node, indent=4))
        args = node.args
        return CallNode(func_name, [self.parse_node(arg) for arg in args])

    def get_str_node(self, node):
        for value in node.values:
            if isinstance(value, ast.FormattedValue):
                answer_node = self.parse_node(value.value)
                if util.is_same_num(answer_node.get_val(), self.original_answer):
                    return answer_node
        raise NotImplementedError("Wrong answer")

    def get_num_node(self, node, _id=None):
        # Check if the number appears in the question
        val = util.to_int_if_int(node.value)
        list_index = util.get_indices_in_list(val, self.nums_in_question)
        if len(list_index) == 0:
            # It is a constant node
            if _id is None:
                _id = next(self.temp_const_name_gen)
            new_node = ConstNode(val)
            self.add_to_dict(_id, new_node, self.constants, True)
        else:
            # It is a variable node
            if _id is None:
                _id = next(self.temp_varname_gen)
            new_node = VarNode(_id, val)
            self.add_to_dict(_id, new_node, self.changeable_variables, True)
            if len(list_index) == 1:
                # Only one node has this value
                self.assign_node[list_index[0]] = new_node
            else:
                for index in list_index:
                    if self.assign_node[index] is None:
                        self.assign_node[index] = new_node
                        # Add to same_num_node
                        if val in self.same_num_nodes:
                            self.same_num_nodes[val].append(index)
                        else:
                            self.same_num_nodes[val] = [index]
                        break
        self.add_to_dict(_id, new_node, self.all_nodes, True)
        return new_node

    def get_unary_node(self, node):
        if isinstance(node.op, ast.USub):
            operand_ast = node.operand
            operand_node = self.parse_node(operand_ast)
            return UnaryOpNode('negate', operand_node)
        raise NotImplementedError(f"node operation has not being implemented: \n{ast.dump(node, indent=4)}")

    def get_binop_node(self, node):
        # Go inside the binary operation first
        left = self.parse_node(node.left)
        right = self.parse_node(node.right)
        # Create the BinOp Node
        res = BinOpNode(self.get_binop(node.op), [left, right])
        return res

    def get_answer(self):
        final_node: BaseNode = self.all_nodes[final_answer_name]
        return final_node.get_val()

    def get_answer_node(self):
        final_node: BaseNode = self.all_nodes[final_answer_name]
        return final_node

    def get_expression(self):
        final_node: BaseNode = self.all_nodes[final_answer_name]
        return str(final_node)

    def get_final_ans(self, node):
        def get_final_ans_binop(_node):
            nodes = [_node.left, _node.right]
            for child in nodes:
                if isinstance(child, ast.BinOp):
                    temp_node, child_found = get_final_ans_binop(child)
                    if child_found:
                        return temp_node, child_found
                if isinstance(child, ast.Call) and child.func.id == 'str':
                    var_node = child.args[0]
                    var_node = self.parse_node(var_node)

                    if var_node is not None and util.is_same_num(var_node.get_val(), self.original_answer):
                        return var_node, True

            return None, False

        answer_node = None

        for arg in node.args:
            if isinstance(arg, ast.Name):
                answer_node = self.parse_node(arg)
            elif isinstance(arg, ast.JoinedStr):
                answer_node = self.parse_node(arg)
            elif isinstance(arg, ast.Call):
                # Formatted string of the form "{}".format(s)
                answer_node = self.get_final_ans(arg)
            elif isinstance(arg, ast.BinOp):
                # print arg of the form "answer is" + str(ans) + "apples."
                answer_node, _ = get_final_ans_binop(arg)

            if answer_node is not None and util.is_same_num(answer_node.get_val(), self.original_answer):
                break

        return answer_node

    @staticmethod
    def get_binop(ast_op):
        if isinstance(ast_op, ast.Add):
            return BinOp.Add
        if isinstance(ast_op, ast.Sub):
            return BinOp.Minus
        if isinstance(ast_op, ast.Mult):
            return BinOp.Mult
        if isinstance(ast_op, ast.Div):
            return BinOp.Divide
        if isinstance(ast_op, ast.FloorDiv):
            return BinOp.FloorDiv
        if isinstance(ast_op, ast.Mod):
            return BinOp.Mod
        raise NotImplementedError(f"Operation {ast_op} is not implemented")

    @staticmethod
    def add_to_dict(key, value, d, can_have_mult=False):
        if key in d and not can_have_mult:
            raise KeyError(f"The key {key} is already in dict")
        elif key in d and can_have_mult:
            orig_key = key
            i = 0
            while orig_key + f'_{i}' in d:
                i += 1
            d[orig_key + f'_{i}'] = d[key]
        d[key] = value
