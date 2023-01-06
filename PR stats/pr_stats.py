import pandas as pd
import requests
from datetime import datetime


def get_pull_requests(owner, repo, github_token):
    # Set up the request headers
    headers = {
        "Authorization": f"Bearer {github_token}"
    }

    # Set up the request parameters
    params = {
        "state": "all",
        "fields": "user,head,base,merged,merged_at,closed_at,comments,reviews"
    }

    # Make the request to the GitHub API
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers=headers,
        params=params
    )

    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful
        pull_requests = response.json()

        # Create a list of dictionaries to hold the pull request data
        data = []
        for pull_request in pull_requests:

            # Get the list of reviewers
            if "reviews" in pull_request:
                reviewers = [review["user"]["login"]
                             for review in pull_request["reviews"]]
            else:
                reviewers = []
            # Get the user name
            if "name" in pull_request["user"]:
                user_name = pull_request["user"]["name"]
            else:
                user_name = None
            # Calculate the lifetime minutes
            if pull_request["state"] == "closed":
                created_at = datetime.strptime(pull_request["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                closed_at = datetime.strptime(pull_request["closed_at"], "%Y-%m-%dT%H:%M:%SZ")
                lifetime_minutes = (closed_at - created_at).total_seconds() / 60
            else:
                lifetime_minutes = None
            # Get the comments for the pull request
            comments_response = requests.get(
                pull_request["comments_url"],
                headers=headers
            )
            if comments_response.status_code == 200:
                # The request was successful
                comments = comments_response.json()
                if len(comments) > 0:
                    # Get the time of the first comment
                    first_comment_time = datetime.strptime(comments[0]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                    # Calculate the first response time
                    first_response_time = (first_comment_time - created_at).total_seconds() / 60
                else:
                    first_comment_time = None
                    first_response_time = None
            else:
                # The request was unsuccessful
                print("An error occurred while fetching the comments")



            data.append({
                "id": pull_request["id"],
                "title": pull_request["title"],
                "state": pull_request["state"],
                "created_at": pull_request["created_at"],
                "updated_at": pull_request["updated_at"],
                "closed_at": pull_request["closed_at"],
                "lifetime_minutes": lifetime_minutes,
                "first_comment_time": first_comment_time,
                "first_response_time":first_response_time,
                "user_login": pull_request["user"]["login"],
                "user_name": user_name,
                "user_avatar_url": pull_request["user"]["avatar_url"],
                "head_ref": pull_request["head"]["ref"],
                "head_sha": pull_request["head"]["sha"],
                "head_repo_name": pull_request["head"]["repo"]["name"],
                "base_ref": pull_request["base"]["ref"],
                "base_sha": pull_request["base"]["sha"],
                "base_repo_name": pull_request["base"]["repo"]["name"],
                "merged_at": pull_request["merged_at"],
                
                "reviewers": reviewers
            })

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(data)

        return df
    else:
        # There was an error making the request
        print(f"Error: {response.status_code}")


def get_project_info(owner, repo, github_token):
    # Set up the request headers
    headers = {
        "Authorization": f"Bearer {github_token}"
    }

    # Set up the request parameters
    params = {
        "fields": "license"
    }

    # Make the request to the GitHub API
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
        params=params
    )

    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        df = pd.DataFrame([data])
        return df
    else:
        # The request was not successful
        df = pd.DataFrame()
        return df
