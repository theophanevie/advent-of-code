from solver.day07_ex1 import Dir, compute_fs, to_delete
from solver.day07_ex2 import dir_to_delete


def test_day07_fs_size():
    root = compute_fs("inputs/input_day07_0", [])

    def test_dir_size(dir: Dir):
        match dir.name:

            case "/":
                assert dir.size == 48381165
            case "a":
                assert dir.size == 94853
            case "e":
                assert dir.size == 584
            case "d":
                assert dir.size == 24933642

        for sub_dir in dir.children:
            test_dir_size(sub_dir)

    test_dir_size(root)


def test_day07_ex1():
    assert to_delete("inputs/input_day07_0") == 95437
    assert to_delete("inputs/input_day07_1") == 1845346


def test_day07_ex2():
    assert dir_to_delete("inputs/input_day07_0") == 24933642
    assert dir_to_delete("inputs/input_day07_1") == 3636703
