import requests
import json

API_key="YTBjMjc5OTUtMDdkYy00YWE2LTkxMTUtYzEzMjZkN2I3Yzkw"
Workspace_id = "63592c1353c3f9136e440670"
#Project_id = "Daily CLI reporter"
test = f'https://reports.api.clockify.me/v1/workspaces/{Workspace_id}/reports/detailed'
def get_summary_forum():
    url = test
    headers = {
        'X-Api-Key': API_key,
        'content-type': 'application/json',
    }
    data = {
        "dateRangeStart": "2022-10-01T00:00:00",
        "dateRangeEnd": "2022-10-28T23:59:59",
        "detailedFilter": {
            "page": 1,
            "pageSize": 50,
            "sortColumn": "DATE"
            },
        
        "exportType": "JSON"
        }

    response = requests.post(url, headers=headers, json=data)
    json_responce = response.json()
    return json_responce


summary = get_summary_forum()
for i in summary["timeentries"]:
    print(i, '\n')