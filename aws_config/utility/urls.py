from django.contrib import admin
from django.urls import path, include
from utility import views

urlpatterns = [
    path("",views.index,name="utility"),
    path("getAllresources",views.get_discovered_resource_counts,name="getAllresources"),
    path("getCompliance",views.describe_compliance_by_resource,name="getCompliance"),
    path("discoverResources",views.get_discovered_resources,name="discoverResources"),
    path("getResourceConfig",views.get_aggregate_resource_config,name="getResourceConfig"),
    path("singleResource",views.discover_single_resource,name="singleResource"),
    path("getSingleResourceConfig",views.get_single_resource_config_request,name="getSingleResourceConfig"),
    path("snapshot",views.take_snaphsot,name="snapshot")
    

    
]
