from typing import List, Tuple

import cotegen.ast_utils as ast_utils

from enum import Enum


class Status(Enum):
    UNEXECUTED = 0
    SURVIVED = 1
    KILLED = 2


class Context():
    def __init__(self, mutation):
        self.ast_node = mutation
        self.ID = None
        self.status = Status.UNEXECUTED
        self.killed_by = []

        self.is_mutant_in_predicate = False
        self.branch_id = None

    def execute(self, test_suite):
        self.status = Status.SURVIVED
        result, killed_by, _ = test_suite.run(self.ast_node)

        if result == 'FAIL':
            self.status = Status.KILLED
            self.killed_by = killed_by

    def print(self, verbose=True):
        print(self.status)
        if self.status == Status.KILLED:
            print('KILLED BY: {} tests'.format(len(self.killed_by)))

        if verbose:
            ast_utils.print_ast(self.ast_node)
            # print('in predicate: ', self.is_mutant_in_predicate)
            # print(self.branch_id)

        print('\n')
