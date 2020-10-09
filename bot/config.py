from bot.sample_config import Config

class Config(Config):
	TG_BOT_TOKEN= "1146934858:AAFfBhyMyMJSdjBVxa8LsQHO3JmF_p6Zdsw"
	APP_ID = 1649008
	API_HASH = "933aae7abdc0b82fffccf3d69d1e7a91"
	OWNER_ID = 1282345589
	AUTH_CHANNEL = [-1001336264133]
	DESTINATION_FOLDER = "bot"
	RCLONE_CONFIG = """type = drive\nclient_id = 1087960453228-1aisiq3pk3u329vmh3rcobnsundcjtee.apps.googleusercontent.com\nclient_secret = sl2iY065FYolOuv38sQ69ln_\nscope = drive\nroot_folder_id = 0AMbxjDSwbyTdUk9PVA\ntoken = {"access_token":"ya29.a0AfH6SMDoX8uS0-4Nupvwe-Q0TsvSTNSZhyf2x-_vD9UuWPr0RyB51qanlkudJozIpIUVv0g4zR1NpmBQrQaOW2KppWCe8OpEOtJHUZGZjUzsINU4QkcSY_3ZTuQn-pzMP4av7UGyJkKOEx-utGi8qTiZfZIDR98sjLw","token_type":"Bearer","refresh_token":"1//0gaAnnW2r-yJLCgYIARAAGBASNwF-L9IryrUE0lLip7ievnLxfL4-jslPc3CgAcvIbPG0eLiTRgln2nu_Z-y19RqyIpD7hQflS7s","expiry":"2020-07-06T01:58:03.627739532+08:00"}"""
	#dont remove """ from both side of the RCLONE_CONFIG
	FINISHED_PROGRESS_STR = "⬛"
	UN_FINISHED_PROGRESS_STR = "⬜"
	INDEX_LINK = "https://files.nuub.workers.dev/1:" 
