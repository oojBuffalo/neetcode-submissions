class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n: int = len(operations)
        record: List[int] = []

        for i in range(n):
            op = operations[i]
            if op.isnumeric() or op[1:].isnumeric():
                record.append(int(operations[i]))
            elif operations[i] == "+":
                if len(record) < 2:
                    raise Exception("Invalid operation: must have at least two scores to perform '+'")
                record.append(record[-2] + record[-1])
            elif operations[i] == "D":
                if len(record) < 1:
                    raise Exception("Invalid operation: must have at least one score to perform 'D'")
                record.append(2 * record[-1])
            elif operations[i] == "C":
                if len(record) < 1:
                    raise Exception("Invalid operation: must have at least one score to perform 'C'")
                record.pop()
            else:
                raise Exception(f"Invalid operation: operation {operations[i]} not recognized")

        return sum(record)