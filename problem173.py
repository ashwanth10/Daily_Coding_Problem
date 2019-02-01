"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
"""
import json

def do_flatten(dictionary):
    answer = {}
    for key in dictionary.keys():
        if 'dict' in str(type(dictionary[key])):
            flatten = do_flatten(dictionary[key])
            for item in flatten.keys():
                answer[key + '.' + item ] = flatten[item]
        else:
            answer[key] = dictionary[key]
    return answer

def main():
    dictionary = raw_input('enter dictionary in string?\n')
    d = json.loads(dictionary)

    print(do_flatten(d))

if __name__ == '__main__':
    main()