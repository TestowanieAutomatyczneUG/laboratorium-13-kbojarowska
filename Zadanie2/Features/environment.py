from src.PasswordValidator import PasswordValidator


def before_scenario(context, scenario):
    context.checkPassword = PasswordValidator()


def after_scenario(context, scenario):
    context.checkPassword = None