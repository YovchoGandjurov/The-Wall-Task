import sys
sys.path.append("..")

from rest_framework.views import APIView
from rest_framework.response import Response

from build_the_wall.main import build_the_wall

profiles = build_the_wall()
PROFILES_LOOKUP = {str(item.number): item for item in profiles}


class ProfilesView(APIView):
    """
    List all profiles including profile sections
    """
    def get(self, request, format=None):
        result = {item.number: str(item.sections) for item in profiles}
        return Response(result)


class IcePerProfilePerDayView(APIView):
    """Ice amount for specific day from specific profile"""

    def get(self, request, prof_number, day):
        result = {
            "day": day,
            "ice_amount": str(PROFILES_LOOKUP[prof_number].ice_specific_day(int(day)))
        }
        return Response(result)


class CostPerProfilePerDay(APIView):
    """Cost for specific day from specific profile"""

    def get(self, request, prof_number, day):
        result = {
            "day": day,
            "ice_amount": str(PROFILES_LOOKUP[prof_number].cost_specific_day(int(day)))
        }
        return Response(result)


class TotalCostPerDayView(APIView):
    """Total cost from all profiles per specific day"""

    def get(self, request, day):
        result = {
            "day": day,
            "ice_amount": str(sum([profile.cost_specific_day(int(day)) for profile in profiles]))
        }
        return Response(result)


class TotalCostView(APIView):
    """Total cost from all profiles per specific day"""

    def get(self, request):
        result = {
            "day": "None",
            "ice_amount": str(sum([profile.total_cost() for profile in profiles]))
        }
        return Response(result)
