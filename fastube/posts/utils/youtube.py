def get_youtube_original_url_by_video_id(video_id):
    return "https://www.youtube.com/watch?v={video_id}".format(
        video_id=video_id
    )


def get_youtube_thumbnail_image_url_by_video_id(video_id):
    return "https://i.ytimg.com/vi/{video_id}/hqdefault.jpg".format(
        video_id=video_id
    )


def get_youtube_embed_url_by_video_id(video_id):
    return "https://www.youtube.com/embed/{video_id}".format(
        video_id=video_id
    )
