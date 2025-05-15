
# RSS to WordPress Poster

## Што прави овој проект:
- Генерира RSS feed од https://www.vesti.mk/category/makedonija
- Автоматски ја објавува првата статија на WordPress

## Како да користиш:
1. Креирај `.env` датотека според `.env.example`
2. Инсталирај ги зависностите: `pip install -r requirements.txt`
3. Стартувај ја скриптата: `python main.py`

## За Railway:
- Deploy на Railway преку zip или GitHub
- Користи `worker` во Procfile
- [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?templateRepo=[streamer-mk/rss-to-wordpress](https://github.com/streamer-mk/rss-to-wordpress)
