import re
import ast


true_responses = [
    'true',
    't',
    'verdadeiro',
    'verdade',
    'y',
    'sim',
    's',
]


def get_list_from_response(response):
    try:
        response = re.sub(r'\s+', ' ', response).strip()
        pattern = r'\[([\s\S]*)\]'
        match = re.search(pattern, response)
        return ast.literal_eval(match.group(0))
    except (AttributeError, SyntaxError, ValueError, TypeError, StopIteration, RuntimeError, KeyError):
        return []


def get_bool_from_response(response):
    response = re.sub(r'\s+', ' ', response).strip()

    if '```' not in response:
        return response.lower() in true_responses
    else:
        try:
            pattern = r'(?<=`)[^`]+(?=`)'
            match = re.search(pattern, response)
            return match.group(0).lower() in true_responses
        except (AttributeError, SyntaxError, ValueError, TypeError, StopIteration, RuntimeError, KeyError):
            return False
