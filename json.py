{
  "name": "Sadboi Userbot",
  "description": "Sadboi Userbot Maded By Lunglung.",
  "logo": "https://telegra.ph/file/84358d66f0e40b1204fda.jpg",
  "keywords": [
    "plugin",
    "modular",
    "productivity"
  ],
  "repository": "https://github.com/ridhoartha/thesadboi/",
  "website": "#TODO",
  "success_url": "#TODO",
  "env": {
    "ALIVE_NAME": {
      "description": "give your name",
      "value": ""
    },
    "APP_ID": {
      "description": "Get this value from my.telegram.org! Please do not steal",
      "value": ""
    },
    "API_HASH": {
      "description": "Get this value from my.telegram.org! Please do not steal",
      "value": ""
    },
    "STRING_SESSION": {
      "description": "Get this value by running python3 telesetup.py locally or https://generatestringsession.sandeep1709.repl.run",
      "value": ""
    },
    "TG_BOT_USERNAME": {
      "description": "Needed for inline buttons maker. Make a bot at http://telegram.dog/BotFather and get the username of your bot",
      "value": ""
    },
    "TG_BOT_TOKEN": {
      "description": "Needed for inline buttons maker. Make a bot at http://telegram.dog/BotFather and get the token of your bot.Worth it. Get it.",
      "value": ""
    },
    "COMMAND_HAND_LER": {
      "description": "Set this one with only one the symbol to use it before your command to run like . , ' `",
      "value": ".",
      "required": false
    },
    "ENV": {
      "description": "Setting this to ANYTHING will enable heroku.",
      "value": "ANYTHING",
      "required": false
    },
    "HEROKU_API_KEY": {
      "description": "Required for updating the bot and other stuff get it from https://dashboard.heroku.com/account",
      "value": "",
      "required": false
    },
    "HEROKU_APP_NAME": {
      "description": "YOUR app name ",
      "value": "",
      "required": false
    },
    "TZ": {
      "description": "Required for Correct Time on autopic/get time. Know your timezone from http://www.timezoneconverter.com/cgi-bin/findzone.tzc",
      "value": "Asia/Kolkata",
      "required": false
    },
    "UPSTREAM_REPO": {
      "description": "Use either goodcat or badcat .if you need custom deploy then type your git repo link",
      "value": "goodcat",
      "required": false
    }
  },
  "addons": [{
    "plan": "heroku-postgresql",
    "options": {
      "version": "12"
    }
  }],
  "buildpacks": [{
    "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest"
  },{
    "url":"https://github.com/heroku/heroku-buildpack-google-chrome"
  },{
    "url":"https://github.com/heroku/heroku-buildpack-chromedriver"
  },{
    "url": "https://github.com/opendoor-labs/heroku-buildpack-p7zip"
  },{
    "url": "https://github.com/heroku/heroku-buildpack-apt.git"
  },{
    "url": "https://github.com/chrismytton/heroku-buildpack-jq"
  },{
    "url": "heroku/python"
  }]
}