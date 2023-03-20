from typing import List
from decorators import to_lists
from profiles_sections import Profile, Section


@to_lists
def read_file(input_file: str) -> List[list]:
    """Read from given file and split the data to lists in list"""
    with open(input_file, "r") as file:
        data = file.readlines()
    return data


def data_to_objects(input_data: List[list]) -> List[Profile]:
    """Transform the raw data to Profile and Section objects"""

    profiles = []
    
    for profile_index, profile_data in enumerate(input_data):
        sections_per_profile = []
        for section_index, section_feet in enumerate(profile_data):
            sections_per_profile.append(Section(section_feet, profile_index+1, section_index+1))
        profiles.append(Profile(profile_index+1, sections_per_profile))
    
    return profiles
