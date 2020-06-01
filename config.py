# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "./"
template = "Kepler"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": True,
    "repo": "wiki-matrix/wikiwiki@gh-pages"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "M@trixのwiki"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2020-05-31T12:00+08:00"
author = "M@trix"
email = "wangwanghello123@gmail.com"
author_homepage = "https://www.blog.hackerjerry.top"
description = "个人知识检索wiki"
key_words = ["Maverick", "M@trix", "wiki", "白帽子"]
language = 'english'
external_links = [
    {
        "name": "Blog",
        "url": "https://www.blog.hackerjerry.top",
        "brief": "Home page for M@trix."
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/wiki-matrix",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "mAY5i7qKOusCTxPVS3GJWSb1-gzGzoHsz",
    "appKey": "0W8KdivYSLCDU361dl2juGqD",
    "visitor": True,
    "recordIP": True
}

head_addon = ''

footer_addon = ''

body_addon = ''
