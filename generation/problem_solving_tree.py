import math
from enum import Enum, auto
from typing import List, Union

import util
from feature_map import FeatureMap


class BaseNode:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = []
        self.parents = []

        # Variables for checking
        self.is_int = None
        self.is_positive = None
        self.is_less_than_one = None
        self.factor_count = None
        self.ten_multiplier = 0
        self.base = None
        self.constraint_count = 6

        self.analyzed = False

        if children:
            self.add_children(children)

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        for child in self.children:
            child.obtain_features(feature_map, "")

    def determine_value_type(self):
        val = self.get_val()
        self.is_int = util.is_int(val)
        self.is_positive = val > 0.0
        self.is_less_than_one = self.is_positive and val < 1.0

        self.value_analysis()

        if self.is_int and self.is_positive:
            self.factor_count = util.get_factor_count(self.base)

        for child in self.children:
            child.determine_value_type()

    def leaf_assign(self, assign_func):
        if self.children:
            for child in self.children:
                child.leaf_assign(assign_func)
        else:
            self.value = assign_func(self.value)

    def value_analysis(self):
        """Define the scientific notations of the node"""
        val = self.get_val()
        base, ten_multiplier = util.get_scientific_notation(val)

        self.base = base
        self.ten_multiplier = ten_multiplier

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
        if self not in child.parents:
            child.parents.append(self)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def get_val(self):
        raise NotImplementedError("BaseNode does not implement get_val")

    def __str__(self):
        raise NotImplementedError("BaseNode does not implement __str__")

    def generate_values(self, generation_method, parent_is_divisor=False):
        for child in self.children:
            child.generate_values(generation_method)

    def get_value_type(self):
        cur_value_type = [True] * self.constraint_count
        for child in self.children:
            child_value_type = child.get_value_type()
            for i in range(self.constraint_count):
                cur_value_type[i] = cur_value_type[i] and child_value_type[i]

        val = self.get_val()
        if not util.is_int(val) and self.is_int:
            cur_value_type[0] = False
        if self.is_positive and val <= 0.0:
            cur_value_type[1] = False
        if self.factor_count is not None:
            new_base, _ = util.get_scientific_notation(val)
            new_factor_count = util.get_factor_count(new_base)
            if self.factor_count >= new_factor_count + 1 and new_factor_count <= 3:
                cur_value_type[3] = False
        if self.is_less_than_one and val >= 1.0:
            cur_value_type[5] = False
        return cur_value_type

    def check_value_type(self, requirement):
        for child in self.children:
            if not child.check_value_type(requirement):
                return False

        val = self.get_val()
        if requirement[0] and not util.is_int(val) and self.is_int:
            return False
        if requirement[1] and self.is_positive and val <= 0.0:
            return False
        if requirement[3] and self.factor_count is not None:
            new_base, _ = util.get_scientific_notation(val)
            new_factor_count = util.get_factor_count(new_base)
            if self.factor_count >= new_factor_count + 1 and new_factor_count <= 3:
                return False
        return True

    def simplify(self):
        for child in self.children:
            child.simplify()

    def has_floor_divide(self):
        has_operator = False
        for child in self.children:
            has_operator = has_operator or child.has_floor_divide()

        return has_operator


class BinOp(Enum):
    Add = auto()
    Minus = auto()
    Mult = auto()
    Divide = auto()
    FloorDiv = auto()
    Mod = auto()


bin_to_string = {
    BinOp.Add: '({0} + {1})',
    BinOp.Minus: '({0} - {1})',
    BinOp.Mult: '({0} * {1})',
    BinOp.Divide: '({0} / {1})',
    BinOp.FloorDiv: '({0} // {1})',
    BinOp.Mod: '({0} % {1})',
}


class BinOpNode(BaseNode):
    def __init__(self, value: BinOp, children: List[BaseNode]):
        if len(children) != 2:
            raise NotImplementedError("Binary operator node should have 2 children")
        # If value is floor divide, check if the code is being safe (10 // 2 = 5)
        #   or it actually utilizes floor divide (10 // 3 = 3)
        lhs = children[0].get_val()
        rhs = children[1].get_val()
        if value == BinOp.FloorDiv and lhs % rhs == 0:
            value = BinOp.Divide

        super().__init__(value, children)

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        feature_map.add_feature(f'{self.value.name}_count', 1)
        feature_map.add_feature(f"operation_count", 1)
        prefix = "inter" if prefix == "" else prefix
        feature_map.add_value_to_feature(self.get_val(), prefix)

        super().obtain_features(feature_map, "")

    def has_floor_divide(self):
        if self.value == BinOp.FloorDiv:
            return True

        return super().has_floor_divide()

    def get_val(self):
        lhs = self.children[0].get_val()
        rhs = self.children[1].get_val()
        if self.value == BinOp.Add:
            return lhs + rhs
        elif self.value == BinOp.Minus:
            return lhs - rhs
        elif self.value == BinOp.Mult:
            return lhs * rhs
        elif self.value == BinOp.Divide:
            return lhs / rhs
        elif self.value == BinOp.Mod:
            return lhs % rhs
        elif self.value == BinOp.FloorDiv:
            return lhs // rhs
        raise NotImplementedError(f"lhs value: {lhs}, rhs value: {rhs}")

    def __str__(self):
        lhs = str(self.children[0])
        rhs = str(self.children[1])
        return bin_to_string[self.value].format(lhs, rhs)

    def simplify(self):
        # Only applies when both children are variables and self value is Divide
        lhs = self.children[0]
        rhs = self.children[1]

        if isinstance(lhs, VarNode) and isinstance(rhs, VarNode) and self.value == BinOp.Divide:
            if util.is_int(lhs.generated_base) and util.is_int(rhs.generated_base):
                lhs.generated_base = int(lhs.generated_base)
                rhs.generated_base = int(rhs.generated_base)

                gcd = math.gcd(lhs.generated_base, rhs.generated_base)

                lhs.generated_base //= gcd
                rhs.generated_base //= gcd
        else:
            super().simplify()

    def generate_values(self, generation_method, parent_is_divisor=False):
        if self.value == BinOp.Divide or self.value == BinOp.FloorDiv:
            self.children[0].generate_values(generation_method)
            self.children[1].generate_values(generation_method)
        else:
            super().generate_values(generation_method, False)


unary_op_map = {
    "negate": lambda x: -x,
}


class UnaryOpNode(BaseNode):
    def __init__(self, value, child: BaseNode):
        super(UnaryOpNode, self).__init__(value, [child])

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        # Check if there is dots in the func name (e.g., math.ceil)
        func_name = self.value.split(".")[-1]
        feature_map.add_feature(f"{func_name}_count", 1)
        feature_map.add_feature(f"operation_count", 1)
        prefix = "inter" if prefix == "" else prefix
        feature_map.add_value_to_feature(self.children[0].get_val(), prefix)

        super().obtain_features(feature_map, "")

    def get_val(self):
        if self.value in unary_op_map:
            # If the operation is pre-defined, get the function and apply to the child
            return unary_op_map[self.value](self.children[0].get_val())
        else:
            # If not, use the value as function name (round, abs) and exec child
            # Might need to import more functions
            val = self.children[0].get_val()
            code = f'import math\nfrom math import *\nlocal_result = {self.value}({val})'
            loc = {}
            exec(code, globals(), loc)
            return loc['local_result']

    def __str__(self):
        return f"{self.value}({self.children[0]})"


class CallNode(BaseNode):
    def __init__(self, value, children):
        super().__init__(value, children)

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        # Check if there is dots in the func name (e.g., math.ceil)
        func_name = self.value.split(".")[-1]
        feature_map.add_feature(f"{func_name}_count", 1)
        prefix = "inter" if prefix == "" else prefix
        feature_map.add_value_to_feature(self.get_val(), prefix)

        super().obtain_features(feature_map, "")

    def get_val(self):
        vals = ", ".join([str(child.get_val()) for child in self.children])
        code = f'import math\nfrom math import *\nlocal_result = {self.value}({vals})'
        loc = {}
        exec(code, globals(), loc)
        return loc['local_result']


class ConstNode(BaseNode):
    def __init__(self, value: Union[int, float]):
        super().__init__(value)

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        feature_map.add_feature(f"const_count", 1)
        prefix = "end" if prefix == "" else prefix
        feature_map.add_value_to_feature(self.value, prefix)

        super().obtain_features(feature_map, "")

    def get_val(self):
        return self.value

    def is_int(self):
        return util.is_int(self.value)

    def set_val(self, value):
        self.value = value

    def is_float(self):
        return isinstance(self.value, (int, float))

    def __str__(self):
        return str(self.value)


class VarNode(BaseNode):
    def __init__(self, var_name: str, value: Union[int, float]):
        super().__init__(var_name)
        self.orig_value = value
        self.generated_base = None
        self.is_scientific = None
        self.is_digits = None

    def obtain_features(self, feature_map: FeatureMap, prefix=""):
        feature_map.add_feature(f"var_count", 1)
        prefix = "end" if prefix == "" else prefix
        feature_map.add_value_to_feature(self.get_val(), prefix)

        super().obtain_features(feature_map, "")

    def get_val(self):
        if self.generated_base is not None:
            return self.get_gen_val()
        return self.orig_value

    def get_gen_val(self):
        if self.is_scientific is not None:
            if self.is_scientific:
                return self.generated_base * 10 ** self.ten_multiplier
            else:
                return self.generated_base
        return None

    def __str__(self):
        return f"{self.value}: ({self.orig_value})({self.get_gen_val()})"

    def set_val(self, value):
        self.is_scientific = False
        self.generated_base = value

    def generate_values(self, generation_method, parent_is_divisor=False):
        req = generation_method
        if req == 'M3':
            gen_method = util.generate_random_num
            args = [self.base]
            self.is_scientific = True
            self.is_digits = True
        elif req == 'M2':
            gen_method = util.get_random_num_with_same_digits
            args = [self.orig_value]
            self.is_scientific = False
            self.is_digits = True
        elif req == 'M1':
            gen_method = util.generate_random_int
            args = [
                1, 100_000 if not parent_is_divisor else 1000,
                self.ten_multiplier if self.ten_multiplier < 0 else None
            ]
            self.is_scientific = False
            self.is_digits = False
        else:
            raise NotImplementedError()

        self.generated_base = gen_method(*args)

    def get_value_type(self):
        cur_value_type = [True, True, self.is_scientific, True, self.is_digits, True]
        val = self.get_val()
        if not util.is_int(val) and self.is_int:
            cur_value_type[0] = False
        if self.is_positive and val <= 0.0:
            cur_value_type[1] = False
        if self.factor_count is not None:
            new_base, _ = util.get_scientific_notation(val)
            new_factor_count = util.get_factor_count(new_base)
            if self.factor_count >= new_factor_count + 1 and new_factor_count <= 3:
                cur_value_type[3] = False
        return cur_value_type
