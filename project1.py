
       
import instaloader
ig=instaloader.Instaloader()
db=input("Enter the instagram id:")
ig.download_profile(db,profile_pic_only=True)

import instaloader
insta=instaloader.Instaloader()
user=input("Enter your instagram username:").lower()
profile=instaloader.Profile.from_username(insta.context,user)
private=profile.is_private
print(private)



