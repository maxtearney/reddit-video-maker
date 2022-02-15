import praw

reddit = praw.Reddit(
    client_id="cNd2mIIhZmzBcsAHeeHo9g",
    client_secret="p68JnkeUTu68IeGavpvzR3OYsQ2O8Q",
    user_agent="<AutoTubeBot-v0.1>"
)

def get_posts(sub, count, span):
    subreddit = reddit.subreddit(sub)
    posts = []
    for submission in subreddit.top(span, limit=count):
        if "r/" not in submission.title and "reddit" not in submission.title:
            posts.append(submission)

    return posts

def get_comments(submission):
    submission.comment_sort = 'best'

    comments = []

    for top_level_comment in submission.comments:
        
        # make sure it's not a link and get top 5 comments
        if "http" not in top_level_comment.body and length(comments) < 5:
            comments.append(top_level_comment)
        elif length(comments) >= 5:
            break

    return comments


posts = get_posts("askreddit")

posts = get_posts("askreddit", 5, "day")

for post in posts:
    print(get_comments(post))