from unittest import TestCase

from typemock import tmock, when
from typemock.api import MemberType, MissingHint, MissingTypeHintsError, MockTypeSafetyError, TypeSafety


class ClassWithNoResponseType:

    def method_with_missing_return_type(self):
        pass


class ClassWithMultipleUnHintedThings:
    hinted_class_att: str = "initial_hinted"
    unhinted_class_att = "initial_not_hinted"
    class_att_with_init_hint = "default"
    class_att_with_unhinted_init = "default2"

    def __init__(
            self,
            class_att_with_init_hint: str,
            class_att_with_unhinted_init,
            instance_att_with_init_hint: str,
            instance_att_with_unhinted_init
    ):
        self.class_att_with_init_hint = class_att_with_init_hint
        self.class_att_with_unhinted_init = class_att_with_unhinted_init
        self.instance_att_with_init_hint = instance_att_with_init_hint
        self.instance_att_with_unhinted_init = instance_att_with_unhinted_init
        self.instance_att_hinted_no_init: int = 0
        self.instance_att_unhinted_no_init = bool

    def _some_private_function(self):
        # We do not care about type hints for private methods
        pass

    def good_method_with_args_and_return(self, number: int) -> str:
        pass

    def good_method_with_no_args_and_return(self) -> str:
        pass

    def method_with_missing_arg_hint(self, something, something_else: bool) -> None:
        pass

    def method_with_missing_return_type(self):
        pass


class MyThing:
    a_hinted_str_attribute: str = "initial"

    def return_a_str(self) -> str:
        pass

    def convert_int_to_str(self, number: int) -> str:
        pass

    def multiple_arg(self, prefix: str, number: int) -> str:
        pass

    def do_something_with_side_effects(self) -> None:
        pass


class TestSafety(TestCase):

    def test_validate_class_type_hints__strict(self):
        expected_missing_type_hints = [
            MissingHint(['class_att_with_unhinted_init'], MemberType.ATTRIBUTE),
            MissingHint(['unhinted_class_att'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_hinted_no_init'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_unhinted_no_init'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_with_unhinted_init'], MemberType.ATTRIBUTE),
            MissingHint(['method_with_missing_arg_hint', 'something'], MemberType.ARG),
            MissingHint(['method_with_missing_return_type'], MemberType.RETURN)
        ]

        with self.assertRaises(MissingTypeHintsError) as error:
            tmock(ClassWithMultipleUnHintedThings, type_safety=TypeSafety.STRICT)
        actual_missing_type_hints = error.exception.args[1]

        self.assertEqual(expected_missing_type_hints, actual_missing_type_hints)

    def test_validate_class_type_hints__no_return_is_none_return(self):
        expected_missing_type_hints = [
            MissingHint(['class_att_with_unhinted_init'], MemberType.ATTRIBUTE),
            MissingHint(['unhinted_class_att'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_hinted_no_init'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_unhinted_no_init'], MemberType.ATTRIBUTE),
            MissingHint(['instance_att_with_unhinted_init'], MemberType.ATTRIBUTE),
            MissingHint(['method_with_missing_arg_hint', 'something'], MemberType.ARG),
        ]

        with self.assertRaises(MissingTypeHintsError) as error:
            tmock(ClassWithMultipleUnHintedThings, type_safety=TypeSafety.NO_RETURN_IS_NONE_RETURN)
        actual_missing_type_hints = error.exception.args[1]

        self.assertEqual(expected_missing_type_hints, actual_missing_type_hints)

    def test_validate_class_type_hints__relaxed(self):
        # Expect no error
        tmock(ClassWithMultipleUnHintedThings, type_safety=TypeSafety.RELAXED)

    def test_try_to_specify_non_type_safe_argument_matching__simple_type(self):
        for type_safety in TypeSafety:
            with self.subTest():
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str("not an int")).then_return("another string")

    def test_try_to_specify_behaviour_with_missing_args(self):
        for type_safety in TypeSafety:
            with self.subTest():
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str()).then_return("another string")

    def test_try_to_specify_behaviour_with_extra_args(self):
        for type_safety in TypeSafety:
            with self.subTest():
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str(1, 2)).then_return("another string")

    def test_try_to_specify_behaviour_with_extra_kwargs(self):
        for type_safety in TypeSafety:
            with self.subTest():
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str(number=1, another=2)).then_return("another string")

    def test_try_to_specify_non_type_safe_return_type__simple_type(self):
        for type_safety in TypeSafety:
            with self.subTest():
                # Method
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str(1)).then_return(2)

                # Attribute get
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.a_hinted_str_attribute).then_return(1)

    def test_try_to_specify_non_type_safe_return_type__simple_type_then_do(self):

        def do_return(*args):
            return 1

        for type_safety in TypeSafety:
            with self.subTest():
                # Method
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str(1)).then_do(do_return)
                    my_thing_mock.convert_int_to_str(1)

                # Attribute get
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.a_hinted_str_attribute).then_do(do_return)
                    my_thing_mock.a_hinted_str_attribute

    def test_try_to_specify_non_type_safe_return_type__simple_type__return_many(self):
        for type_safety in TypeSafety:
            with self.subTest():
                with self.assertRaises(MockTypeSafetyError):
                    with tmock(MyThing, type_safety=type_safety) as my_thing_mock:
                        when(my_thing_mock.convert_int_to_str(1)).then_return_many(["okay", 1])

    def test_try_to_set_attribute_with_incorrect_type(self):
        for type_safety in TypeSafety:
            with self.subTest():
                my_thing_mock = tmock(MyThing, type_safety=type_safety)

                # Method
                with self.assertRaises(MockTypeSafetyError):
                    my_thing_mock.a_hinted_str_attribute = 1

    # TODO: Recursive type safety for nested objects (only their attributes and properties).


class TestTypeSafetyRelaxed(TestCase):

    def test_specify_behaviour_of_non_hinted_arg(self):
        with tmock(ClassWithMultipleUnHintedThings, type_safety=TypeSafety.RELAXED) as my_mock:
            when(my_mock.method_with_missing_arg_hint("could_be_anything", True)).then_return(None)

    def test_specify_return_of_non_hinted_return(self):
        with tmock(ClassWithMultipleUnHintedThings, type_safety=TypeSafety.RELAXED) as my_mock:
            when(my_mock.method_with_missing_return_type()).then_return("something")


class TestTypeSafetyNoResponseIsNone(TestCase):

    def test_specify_return_to_be_None_when_missing(self):
        with tmock(ClassWithNoResponseType, type_safety=TypeSafety.NO_RETURN_IS_NONE_RETURN) as my_mock:
            when(my_mock.method_with_missing_return_type()).then_return(None)

    def test_specify_return_to_be_something_elsewhen_missing(self):
        with self.assertRaises(MockTypeSafetyError):
            with tmock(ClassWithNoResponseType, type_safety=TypeSafety.NO_RETURN_IS_NONE_RETURN) as my_mock:
                when(my_mock.method_with_missing_return_type()).then_return("Something")
