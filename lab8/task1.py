from dsmltf import build_tree_id3, train_test_split

from lab8.support_methods import test_classify
from supporting.split_dataset import train_test_dataset_split


def solve():
    # Строим датасет
    dataset = [
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090301", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090304", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "100503", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, True),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090301", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "yes", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "good"}, False),
        ({"program": "090304", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "100503", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "no", "teacher_feedback": "good"}, True),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "yes", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "good"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "no", "attendance_class": "less 30%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "100503", "past_debt": "no", "earlier_debt": "no", "attendance_class": "50% to 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "yes", "active_in_events": "yes", "teacher_feedback": "excellent"}, True),
        ({"program": "090304", "past_debt": "yes", "earlier_debt": "yes", "attendance_class": "30% to 50%", "vk_registered": "no", "classroom_registered": "no", "athlete": "no", "active_in_events": "no", "teacher_feedback": "bad"}, False),
        ({"program": "090301", "past_debt": "no", "earlier_debt": "no", "attendance_class": "more 80%", "vk_registered": "yes", "classroom_registered": "yes", "athlete": "no", "active_in_events": "yes", "teacher_feedback": "excellent"}, True)
    ]

    train_dataset, test_dataset = train_test_dataset_split(dataset)

    # Строим ДПР (Дерево Принятия Решений)
    tree = build_tree_id3(train_dataset)

    # Находим количество верных предсказаний на тестовой выборке
    correct_predictions, all_predictions = test_classify(tree, test_dataset)

    # Выводим результаты
    res = round(correct_predictions / all_predictions, 4) * 100
    print(f"Результаты теста: {correct_predictions}/{all_predictions} ({res})")
