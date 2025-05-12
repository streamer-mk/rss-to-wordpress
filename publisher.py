
import requests
import os

def post_to_wordpress(title, content, image_url=None):
    wp_url = os.getenv("WP_SITE_URL")
    wp_user = os.getenv("WP_USERNAME")
    wp_pass = os.getenv("WP_PASSWORD")

    media_id = None
    if image_url:
        img_data = requests.get(image_url).content
        img_name = image_url.split("/")[-1]
        media = requests.post(
            wp_url + "/wp-json/wp/v2/media",
            headers={
                "Content-Disposition": f"attachment; filename={img_name}"
            },
            data=img_data,
            auth=(wp_user, wp_pass)
        )
        if media.ok:
            media_id = media.json().get("id")

    post_data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    if media_id:
        post_data["featured_media"] = media_id

    response = requests.post(
        wp_url + "/wp-json/wp/v2/posts",
        json=post_data,
        auth=(wp_user, wp_pass)
    )
    return response
