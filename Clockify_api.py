import requests
import json
import pandas

API_key="YTBjMjc5OTUtMDdkYy00YWE2LTkxMTUtYzEzMjZkN2I3Yzkw"#user API key
Workspace_id = requests.get("https://api.clockify.me/api/v1/user", headers={'X-Api-Key': API_key}).json()['activeWorkspace']

clock_url = f'https://reports.api.clockify.me/v1/workspaces/{Workspace_id}/reports/detailed'

def get_summary_forum():
    url = clock_url
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
    json_response = response.json()
    return json_response


def detailed_report(data):
    keys_to_pop = ['_id', 'userId', 'billable', 'taskId', 'approvalRequestId', 'tags', 'projectId', 'isLocked', 'customFields', 'projectColor', 'rate', 'userEmail', 'clientId']
    df = pandas.DataFrame(data['timeentries'])
    
    df = df.drop(keys_to_pop, axis=1)
    df['taskDuration'] = [el['timeInterval']['duration'] for el in data["timeentries"]]
    print(df)
    df.to_csv('report.csv', sep=',', encoding='cp1251')


if __name__ == "__main__":
    summary = get_summary_forum()
    detailed_report(summary)