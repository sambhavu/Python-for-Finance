from instapy import InstaPy

session = InstaPy(username = "", password = "")
session.login() 

session.like_by_tage(["mercedes", "bmw"], amount = 5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage = 50)
session.set_do_comment(True, percentage = 50)
session.set_comments(["Cute!", "Beautiful :hear_eyes:", "Nice!"])
session.set_quota_supervisor(enabled = True, peak_comments_daily = 240, peak_comments_hourly = 30)
session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
session.clarifai_check_img_for(['nsfw'])

