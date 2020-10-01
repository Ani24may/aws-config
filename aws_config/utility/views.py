from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import boto3
import json

# Create your views here.
global config
config = boto3.client('config')
def index(request):
    return HttpResponse("test")

def get_discovered_resources(request):
    response = config.get_discovered_resource_counts(
    resourceTypes=[
      
    ],
    limit=100)
    jsonObject=json.loads(json.dumps(response))
    discover_resources=[]
    data={}
    for r in jsonObject["resourceCounts"]:
        discover_resources.append(list_discovered_resources(r["resourceType"]))
    data["resources"]=discover_resources
    #print(data)
    return HttpResponse(json.dumps(data))

@csrf_exempt 
def discover_single_resource(request):
    jsonObject=list_discovered_resources(request.POST["reosource"])
    return HttpResponse(json.dumps(jsonObject))

def list_discovered_resources(resource_name):
    response = config.list_discovered_resources(
    resourceType=resource_name,
    limit=0)
    jsonObject=json.loads(json.dumps(response["resourceIdentifiers"]))
    return jsonObject

def get_discovered_resource_counts(request):
    #config = boto3.client('config')
    
    #print(jsonObject["resourceCounts"])
    response = config.get_discovered_resource_counts(
    resourceTypes=[
      
    ],
    limit=100)
    jsonObject=json.loads(json.dumps(response))
    return HttpResponse(json.dumps(response))

def describe_compliance_by_resource(request):
    response1 = config.get_discovered_resource_counts(
    resourceTypes=[
      
    ],
    limit=100)
    jsonObject=json.loads(json.dumps(response1))
    discover_resources=[]
    data={}
    for r in jsonObject["resourceCounts"]:
        response = config.describe_compliance_by_resource(
        ResourceType=r["resourceType"],
        ComplianceTypes=[
            'COMPLIANT','NON_COMPLIANT',
        ],
        Limit=100)
        discover_resources.append(json.loads(json.dumps(response["ComplianceByResources"])))
    data["ComplianceByResources"]=discover_resources
    return HttpResponse(json.dumps(data))

def get_aggregate_resource_config(request):
    response = config.get_discovered_resource_counts(
    resourceTypes=[
      
    ],
    limit=100)
    jsonObject=json.loads(json.dumps(response))
    discover_resources=[]
    discover_resources_config=[]
    resources_config={}
    data={}
    for r in jsonObject["resourceCounts"]:
        discover_resources.append(list_discovered_resources(r["resourceType"]))
    # data["resources"]=discover_resources
    for all_resources in discover_resources:
        for s in all_resources:
            #print(s["resourceType"]+s["resourceId"])
            response=get_single_resource_config(s["resourceId"], s["resourceType"])
            discover_resources_config.append(response)
    resources_config["resources_config"]=discover_resources_config
    return HttpResponse(resources_config)

def get_single_resource_config(resource_Id,resource_type):
    response = config.get_aggregate_resource_config(
        ConfigurationAggregatorName='aws-config-aggregator',
        ResourceIdentifier={
            'SourceAccountId': '933021275826',
            'SourceRegion': 'us-east-1',
            'ResourceId': resource_Id,
            'ResourceType': resource_type
        })
    return response

@csrf_exempt
def get_single_resource_config_request(request):
    response=get_single_resource_config(request.POST["reosource_id"],request.POST["reosource_type"])
    return HttpResponse(str(response))

def take_snaphsot(request):
#     response=config.describe_delivery_channels(
#    )
    response = config.deliver_config_snapshot(
    deliveryChannelName='default')

    return HttpResponse(str(response))






