class Solution:
    def isValid(self, s: str) -> bool:
        output = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                output.append(i)

            elif i == ")":
                if not output:
                    return False
                if output[-1] == "(":
                    output.pop()
                else:
                    return False

            elif i == "}":
                if not output:
                    return False
                if output[-1] == "{":
                    output.pop()
                else:
                    return False

            elif i == "]":
                if not output:
                    return False
                if output[-1] == "[":
                    output.pop()
                else:
                    return False

            else:
                return False

        return len(output) == 0