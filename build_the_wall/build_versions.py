import logging
from typing import List

import multiprocessing as mp

import config
from constants import CUBIC_YARDS_PER_DAY, GOLD_DRAGON_COIN
from profiles_sections import Profile, Section
from multiprocessing_helpers import Consumer, Task

logging.getLogger().setLevel(logging.DEBUG)


def build_single_process(profiles: List[Profile]) -> List[Profile]:
    """
    Iterate over all profiles and build section by section until all of them reach 30 feet
    """

    while True:
        for profile in profiles:
            for section in profile.sections:
                section.build()

        if all([profile.is_finished() for profile in profiles]):
            break

    return profiles


def build_multiprocessing(profiles: List[Profile]):
    """
    Create a list of process objects named Consumer in order to pick one task (section).
    There are two queues, task_q - all initial sections and output_q that collect all processed sections.
    At the end, we need to rebuild a collection containing all the profiles with their sections.
    """
    all_section = [section for profile in profiles for section in profile.sections]

    task_q = mp.JoinableQueue()
    output_q = mp.Queue()
    
    for section in all_section:
        task_q.put(Task(section))
    
    consumers = [Consumer(task_q, output_q, n+1) for n in range(config.PROCESSES)]
    
    for consumer in consumers:
        logging.debug(f"Consumer {consumer.consumer_number} started")
        consumer.start()

    task_q.join()
    
    for i, consumer in enumerate(consumers):
        logging.debug(f"Consumer {i} killed")
        consumer.kill()
    
    built_sections = [output_q.get().section for _ in range(output_q.qsize())]
    profiles = _from_sections_to_profiles(built_sections)
    
    return profiles


def _from_sections_to_profiles(sections: List[Section]) -> List[Profile]:
    """Transform all processed section to profile objects contains thairs sections"""
    
    profiles_dict = {}
    for section in sections:
        if section.profile_number in profiles_dict:
            profiles_dict[section.profile_number].append(section)
        else:
            profiles_dict[section.profile_number] = [section]
    
    return [Profile(key, sorted(value, key=lambda x: x.section_position)) for key, value in profiles_dict.items()]
