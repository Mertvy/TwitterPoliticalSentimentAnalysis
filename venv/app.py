from flask import Flask, request
import openai
from TweetClassifier import single_classifier
from filtered_stream import clean_slate

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    return """
        <html>
        <head>
        <style>
        * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: "Roboto", sans-serif;
}

body {
  background-color: #f7f8f9;
  color: #0f1419;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  -webkit-tap-highlight-color: transparent;
}

a {
  text-decoration: none;
  font: inherit;
  color: inherit;
}

.bar {
  height: 8px;
  background-color: #1da1f2;
  background: linear-gradient(to right, #00c6ff, #0072ff);
}

header {
  padding: 32px 16px;
  text-align: center;
}
header h1 {
  font-size: 48px;
  font-weight: 500;
}
@media (max-width: 640px) {
  header h1 {
    font-size: 38px;
  }
}
@media (max-width: 520px) {
  header h1 {
    font-size: 32px;
  }
}

main {
  flex: 1;
  max-width: 1024px;
  width: 100%;
  margin: auto;
  padding: 32px 16px;
  display: flex;
  align-items: flex-start;
}
main .form {
  background-color: white;
  border: 1px #dde7ef solid;
  border-radius: 8px;
  padding: 24px;
  flex: 1;
}
main .form h2 {
  font-size: 22px;
  font-weight: 500;
  margin-bottom: 32px;
}
main .form .form-control {
  margin-bottom: 24px;
}
main .form .form-control:last-child {
  margin-bottom: 2px;
}
main .form .form-control label {
  display: block;
  font-weight: 500;
}
main .form .form-control input,
main .form .form-control textarea {
  display: block;
  font: inherit;
  width: 100%;
  padding: 10px 14px;
  margin: 4px 0;
  border: 1px #cbd5e1 solid;
  border-radius: 6px;
  outline: none;
  transition: border-color 200ms ease-in;
}
main .form .form-control input:focus,
main .form .form-control textarea:focus {
  border-color: #1da1f2;
}
main .form .form-control input::placeholder,
main .form .form-control textarea::placeholder {
  color: #9ca1a5;
}
main .form .form-control textarea {
  resize: vertical;
}
main .form .form-control small {
  font-size: 13px;
  color: #8c9094;
}
main .form .form-control .username_input {
  display: block;
  background-color: white;
  color: #8c9094;
  font: inherit;
  width: 100%;
  padding: 0 14px;
  margin: 4px 0;
  border: 1px #cbd5e1 solid;
  border-radius: 6px;
  outline: none;
  transition: border-color 200ms ease-in, color 200ms ease-in;
  display: flex;
  align-items: center;
}
main .form .form-control .username_input:focus-within {
  border-color: #1da1f2;
  color: #0f1419;
}
main .form .form-control .username_input::placeholder {
  color: #9ca1a5;
}
main .form .form-control .username_input input {
  display: inline;
  margin: 0 0 0 2px;
  padding: 10px 0;
  border: none;
}
main .form .form-control input[type=radio] {
  display: inline;
  width: fit-content;
}
main .form .form-control input[type=radio] + label {
  display: inline;
}
main .form .form-control p {
  font-weight: 500;
}
main .form .form-control .group {
  margin-top: 10px;
  display: flex;
}
main .form .form-control .group .radio_container {
  display: block;
  position: relative;
  padding-left: 22px;
  margin-right: 20px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 400;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
main .form .form-control .group .radio_container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
main .form .form-control .group .radio_mark {
  position: absolute;
  top: 1px;
  left: 0;
  height: 16px;
  width: 16px;
  border: 1px #aab8c2 solid;
  border-radius: 50%;
  background-color: white;
}
main .form .form-control .group .radio_container input:focus ~ .radio_mark {
  box-shadow: 0 0 0 3px rgba(29, 161, 242, 0.4);
}
main .form .form-control .group .radio_container input:checked ~ .radio_mark {
  background-color: #1da1f2;
  border-color: #1da1f2;
}
main .form .form-control .group .radio_mark:after {
  content: "";
  position: absolute;
  display: none;
}
main .form .form-control .group .radio_container input:checked ~ .radio_mark:after {
  display: block;
}
main .form .form-control .group .radio_container .radio_mark:after {
  top: 3px;
  left: 3px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: white;
}
main .form .form-control.upload {
  margin-bottom: 42px;
  display: flex;
  position: relative;
}
main .form .form-control.upload label {
  display: inline-block;
  position: relative;
  border-radius: 99px;
  background-color: #1da1f2;
  color: #fff;
  font-weight: 400;
  padding: 10px 30px;
  cursor: pointer;
}
@media (hover: hover) {
  main .form .form-control.upload label {
    transition: background 200ms ease-in;
  }
  main .form .form-control.upload label:hover {
    background-color: #1a90d9;
  }
}
@media (hover: none) {
  main .form .form-control.upload label:active {
    background-color: #1a90d9;
  }
}
main .form .form-control.upload .file {
  opacity: 0;
  width: 0;
  height: 0;
  position: absolute;
  top: 0;
  left: 0;
  cursor: pointer;
  z-index: -10;
}
main .form .form-control.upload .file-name {
  font-size: 13px;
  font-weight: 400;
  position: absolute;
  bottom: -29px;
  background-color: #eef3f7;
  color: #0f1419;
  border-radius: 99px;
  padding: 4px 16px;
  display: none;
}
main .form .form-control.upload .file-name.show {
  display: block;
}
main .form .form-control.upload .reset {
  border: 1px #1da1f2 solid;
  border-radius: 99px;
  background-color: white;
  color: #1da1f2;
  font: inherit;
  cursor: pointer;
  padding: 10px 30px;
  margin-left: 12px;
}
@media (hover: hover) {
  main .form .form-control.upload .reset {
    transition: background 200ms ease-in;
  }
  main .form .form-control.upload .reset:hover {
    background-color: #e6e8eb;
  }
}
@media (hover: none) {
  main .form .form-control.upload .reset:active {
    background-color: #e6e8eb;
  }
}
@media (max-width: 890px) {
  main .form {
    width: 75%;
    margin: 0 auto;
  }
}
@media (max-width: 700px) {
  main .form {
    width: 85%;
    margin: 0 auto;
  }
}
@media (max-width: 640px) {
  main .form {
    width: 95%;
    margin: 0 auto;
  }
}
@media (max-width: 520px) {
  main .form {
    background-color: #f7f8f9;
    width: 100%;
    margin: 0 auto;
    box-shadow: none;
    border: none;
    border-radius: 0;
    padding: 24px 0;
  }
}
main .tweet-desk {
  background-color: white;
  border: 1px #dde7ef solid;
  border-radius: 8px;
  padding: 24px;
  margin-left: 16px;
  position: sticky;
  top: 16px;
  z-index: 10;
}
main .tweet-desk h2 {
  font-size: 22px;
  font-weight: 500;
}
main .tweet-desk .tweet_box {
  border: 1px #eff3f4 solid;
  background-color: white;
  margin: 32px 0 34px;
  width: 440px;
}
main .tweet-desk .tweet_box.dim {
  border: 1px #15202b solid;
  background-color: #15202b;
}
main .tweet-desk .tweet_box.dark {
  border: 1px #000000 solid;
  background-color: #000000;
}
@media (max-width: 940px) {
  main .tweet-desk .tweet_box {
    width: 400px;
  }
}
@media (max-width: 890px) {
  main .tweet-desk .tweet_box {
    max-width: 440px;
    width: 100%;
    margin: 32px auto;
  }
}
main .tweet-desk .tweet {
  border: 1px transparent solid;
  background-color: white;
  padding: 0 16px;
  font-size: 15px;
  width: 100%;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
main .tweet-desk .tweet .head {
  padding-top: 12px;
  display: flex;
  justify-content: space-between;
}
main .tweet-desk .tweet .head .title {
  display: flex;
  align-items: center;
}
main .tweet-desk .tweet .head .title img {
  display: inline-block;
  border-radius: 50%;
  margin-right: 12px;
}
main .tweet-desk .tweet .head .title .text .top {
  font-weight: 700;
  display: flex;
  align-items: center;
}
main .tweet-desk .tweet .head .title .text .top .tweet_name {
  margin-right: 2px;
}
main .tweet-desk .tweet .head .title .text .top .verified {
  font-weight: 400;
  color: #1da1f2;
}
main .tweet-desk .tweet .head .title .text .top .verified.hide {
  display: none;
}
main .tweet-desk .tweet .head .title .text .bottom {
  color: #536471;
}
main .tweet-desk .tweet .head .dots {
  color: #536471;
}
main .tweet-desk .tweet .content .message {
  padding-top: 16px;
  font-size: 23px;
}
main .tweet-desk .tweet .content .message .highlight {
  color: #1b95e0;
}
main .tweet-desk .tweet .content .tweet_info {
  color: #536471;
  padding: 16px 0;
  display: flex;
}
main .tweet-desk .tweet .stats {
  border-top: 1px #eff3f4 solid;
  color: #536471;
  padding: 16px 4px;
  display: flex;
  flex-wrap: wrap;
}
main .tweet-desk .tweet .stats .stat {
  margin-right: 24px;
}
main .tweet-desk .tweet .stats .stat .count {
  font-weight: 700;
  color: #0f1419;
}
main .tweet-desk .tweet .stats .stat.hide {
  display: none;
}
@media (max-width: 520px) {
  main .tweet-desk .tweet .stats .stat {
    margin-right: 12px;
  }
}
main .tweet-desk .tweet .tail {
  border-top: 1px #eff3f4 solid;
  padding: 12px 0;
  display: flex;
  justify-content: space-around;
}
main .tweet-desk .tweet .tail svg {
  color: #536471;
}
main .tweet-desk .tweet.dim {
  background-color: #15202b;
  color: white;
}
main .tweet-desk .tweet.dim .head .title .text .top .verified {
  color: white;
}
main .tweet-desk .tweet.dim .head .title .text .bottom,
main .tweet-desk .tweet.dim .head .title .text .dots {
  color: #798a96;
}
main .tweet-desk .tweet.dim .content .tweet_info {
  color: #798a96;
}
main .tweet-desk .tweet.dim .content .tweet_info .tweet_client {
  color: #1b95e0;
}
main .tweet-desk .tweet.dim .stats {
  border-top: 1px #38444d solid;
  color: #798a96;
}
main .tweet-desk .tweet.dim .stats .stat .count {
  color: white;
}
main .tweet-desk .tweet.dim .tail {
  border-top: 1px #38444d solid;
}
main .tweet-desk .tweet.dim .tail svg {
  color: #798a96;
}
main .tweet-desk .tweet.dark {
  background-color: #000000;
  color: #d9d9d9;
}
main .tweet-desk .tweet.dark .head .title .text .top .verified {
  color: #d9d9d9;
}
main .tweet-desk .tweet.dark .head .title .text .bottom,
main .tweet-desk .tweet.dark .head .title .text .dots {
  color: #6e767d;
}
main .tweet-desk .tweet.dark .content .tweet_info {
  color: #6e767d;
}
main .tweet-desk .tweet.dark .content .tweet_info .tweet_client {
  color: #1b95e0;
}
main .tweet-desk .tweet.dark .stats {
  border-top: 1px #2f3336 solid;
  color: #6e767d;
}
main .tweet-desk .tweet.dark .stats .stat .count {
  color: #d9d9d9;
}
main .tweet-desk .tweet.dark .tail {
  border-top: 1px #2f3336 solid;
}
main .tweet-desk .tweet.dark .tail svg {
  color: #6e767d;
}
@media (max-width: 395px) {
  main .tweet-desk .tweet {
    font-size: 14px;
  }
  main .tweet-desk .tweet .content .message {
    font-size: 21px;
  }
  main .tweet-desk .tweet .stats {
    padding: 16px 0;
  }
  main .tweet-desk .tweet .stats .stat {
    margin-right: 8px;
  }
}
main .tweet-desk .btn {
  display: block;
  border: none;
  border-radius: 6px;
  border-radius: 99px;
  background-color: #1da1f2;
  color: white;
  font: inherit;
  margin: auto;
  padding: 11px 33px;
  cursor: pointer;
}
@media (hover: hover) {
  main .tweet-desk .btn {
    transition: background 200ms ease-in;
  }
  main .tweet-desk .btn:hover {
    background-color: #1a90d9;
  }
}
@media (hover: none) {
  main .tweet-desk .btn:active {
    background-color: #1a90d9;
  }
}
@media (max-width: 890px) {
  main .tweet-desk {
    width: 75%;
    margin: 0 auto 16px;
    position: static;
  }
}
@media (max-width: 700px) {
  main .tweet-desk {
    width: 85%;
    margin: 0 auto 16px;
  }
}
@media (max-width: 640px) {
  main .tweet-desk {
    width: 95%;
    margin: 0 auto 16px;
  }
}
@media (max-width: 520px) {
  main .tweet-desk {
    background-color: #f7f8f9;
    width: 100%;
    margin: 0 auto 16px;
    box-shadow: none;
    border: none;
    border-radius: 0;
    padding: 24px 0;
  }
}
@media (max-width: 890px) {
  main {
    flex-direction: column-reverse;
  }
}
@media (max-width: 520px) {
  main {
    padding: 16px;
  }
}

footer {
  padding: 32px 16px;
  font-size: 14px;
  font-weight: 400;
  color: #6e8698;
  display: flex;
  justify-content: center;
  align-items: center;
}
footer .foot {
  text-align: center;
}
footer .foot a {
  border-bottom: 1px #6e8698 dotted;
}
@media (hover: hover) {
  footer .foot a:hover {
    border-bottom-style: solid;
  }
}
@media (hover: none) {
  footer .foot a:active {
    border-bottom-style: solid;
  }
}
footer .dot {
  width: 3px;
  height: 3px;
  background-color: #6e8698;
  border-radius: 50%;
  margin: 0 6px;
}

        </style>
        </head>
        <body>
            <textarea id="prompt"></textarea>
            <button onclick="generateResponse()">Generate Response</button>
            <div id="response"></div>
            """ + TwitterPostFromJSON(single_classifier(clean_slate())) + """
            <button class="refresh">CLICK ME</button>
            <script>
              async function generateResponse() {
                fetch("/response", {
                    method: "POST",
                     headers: {
                    "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        prompt: document.getElementById("prompt").value
                    })
                })
                .then(response => response.text())
                .then(response => {
                    document.getElementById("response").innerHTML = response;
                });
              }
            </script>
        </body>
        </html>
    """

@app.route("/response", methods=["POST"])
def response():
    prompt = request.get_json()["prompt"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

def TwitterPostFromJSON(input):
    output = f'''
    <main>
        <div class="tweet-desk">
          <h2>Preview</h2>
          <div id="tweet_box" class="tweet_box">
            <div id="tweet" class="tweet">
                <div class="head">
                  <div class="title">
                    <img id="tweet_avatar" src="https://e7.pngegg.com/pngimages/595/477/png-clipart-twitter-logo-computer-icons-logo-twitter-miscellaneous-monochrome.png" alt="avatar" width="48" height="48">
                    <div class="text">
                      <div class="top">
                        <span class="tweet_name" id="tweet_name">{input[0][1]}</span>
                        <svg xmlns="http://www.w3.org/2000/svg" id="tweet_verified" class="verified" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                          <g>
                            <path d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.71-3.998-3.818-3.998-.47 0-.92.084-1.336.25C14.818 2.415 13.51 1.5 12 1.5s-2.816.917-3.437 2.25c-.415-.165-.866-.25-1.336-.25-2.11 0-3.818 1.79-3.818 4 0 .494.083.964.237 1.4-1.272.65-2.147 2.018-2.147 3.6 0 1.495.782 2.798 1.942 3.486-.02.17-.032.34-.032.514 0 2.21 1.708 4 3.818 4 .47 0 .92-.086 1.335-.25.62 1.334 1.926 2.25 3.437 2.25 1.512 0 2.818-.916 3.437-2.25.415.163.865.248 1.336.248 2.11 0 3.818-1.79 3.818-4 0-.174-.012-.344-.033-.513 1.158-.687 1.943-1.99 1.943-3.484zm-6.616-3.334l-4.334 6.5c-.145.217-.382.334-.625.334-.143 0-.288-.04-.416-.126l-.115-.094-2.415-2.415c-.293-.293-.293-.768 0-1.06s.768-.294 1.06 0l1.77 1.767 3.825-5.74c.23-.345.696-.436 1.04-.207.346.23.44.696.21 1.04z"></path>
                          </g>
                        </svg>
                      </div>
                      <div class="bottom">
                        @<span id="tweet_username">{input[0][0]}</span>
                      </div>
                    </div>
                  </div>
                  <div class="dots">
                    <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="currentColor">
                      <g>
                        <circle cx="5" cy="12" r="2"></circle>
                        <circle cx="12" cy="12" r="2"></circle>
                        <circle cx="19" cy="12" r="2"></circle>
                      </g>
                    </svg>
                  </div>
                </div>
                <div class="content">
                  <div id="tweet_message" class="message">{input[0][2]}</div>
                  <div class="tweet_info">
                    <div id="tweet_time">{input[0][4][1]}</div>
                    &nbsp;·&nbsp;
                    <div id="tweet_date">{input[0][4][0]}</div>
                    &nbsp;·&nbsp;
                    <div id="tweet_client" class="tweet_client">{input[0][3]}</div>
                  </div>
                </div>
                <div class="stats">
                  <div class="stat">
                    <span id="tweet_retweets" class="count">{input[1][0].confidence*100}%</span> Degree of Hate-speech
                  </div>
                  <div class="stat">
                    <span id="tweet_quotes" class="count">{input[2][0].confidence*100}%</span> Leans Democrat
                  </div>
                  <div class="stat">
                    <span id="tweet_likes" class="count">{(1-input[2][0].confidence)*100}%</span> Leans Republican
                  </div>
                </div>
                <div class="tail">
                  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                    <g>
                      <path d="M14.046 2.242l-4.148-.01h-.002c-4.374 0-7.8 3.427-7.8 7.802 0 4.098 3.186 7.206 7.465 7.37v3.828c0 .108.044.286.12.403.142.225.384.347.632.347.138 0 .277-.038.402-.118.264-.168 6.473-4.14 8.088-5.506 1.902-1.61 3.04-3.97 3.043-6.312v-.017c-.006-4.367-3.43-7.787-7.8-7.788zm3.787 12.972c-1.134.96-4.862 3.405-6.772 4.643V16.67c0-.414-.335-.75-.75-.75h-.396c-3.66 0-6.318-2.476-6.318-5.886 0-3.534 2.768-6.302 6.3-6.302l4.147.01h.002c3.532 0 6.3 2.766 6.302 6.296-.003 1.91-.942 3.844-2.514 5.176z"></path>
                    </g>
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                    <g>
                      <path d="M23.77 15.67c-.292-.293-.767-.293-1.06 0l-2.22 2.22V7.65c0-2.068-1.683-3.75-3.75-3.75h-5.85c-.414 0-.75.336-.75.75s.336.75.75.75h5.85c1.24 0 2.25 1.01 2.25 2.25v10.24l-2.22-2.22c-.293-.293-.768-.293-1.06 0s-.294.768 0 1.06l3.5 3.5c.145.147.337.22.53.22s.383-.072.53-.22l3.5-3.5c.294-.292.294-.767 0-1.06zm-10.66 3.28H7.26c-1.24 0-2.25-1.01-2.25-2.25V6.46l2.22 2.22c.148.147.34.22.532.22s.384-.073.53-.22c.293-.293.293-.768 0-1.06l-3.5-3.5c-.293-.294-.768-.294-1.06 0l-3.5 3.5c-.294.292-.294.767 0 1.06s.767.293 1.06 0l2.22-2.22V16.7c0 2.068 1.683 3.75 3.75 3.75h5.85c.414 0 .75-.336.75-.75s-.337-.75-.75-.75z"></path>
                    </g>
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                    <g>
                      <path d="M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.037 13.157H12zM7.354 4.225c-2.08 0-3.903 1.988-3.903 4.255 0 5.74 7.034 11.596 8.55 11.658 1.518-.062 8.55-5.917 8.55-11.658 0-2.267-1.823-4.255-3.903-4.255-2.528 0-3.94 2.936-3.952 2.965-.23.562-1.156.562-1.387 0-.014-.03-1.425-2.965-3.954-2.965z"></path>
                    </g>
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                    <g>
                      <path d="M17.53 7.47l-5-5c-.293-.293-.768-.293-1.06 0l-5 5c-.294.293-.294.768 0 1.06s.767.294 1.06 0l3.72-3.72V15c0 .414.336.75.75.75s.75-.336.75-.75V4.81l3.72 3.72c.146.147.338.22.53.22s.384-.072.53-.22c.293-.293.293-.767 0-1.06z"></path>
                      <path d="M19.708 21.944H4.292C3.028 21.944 2 20.916 2 19.652V14c0-.414.336-.75.75-.75s.75.336.75.75v5.652c0 .437.355.792.792.792h15.416c.437 0 .792-.355.792-.792V14c0-.414.336-.75.75-.75s.75.336.75.75v5.652c0 1.264-1.028 2.292-2.292 2.292z"></path>
                    </g>
                  </svg>
                </div>
              </div>
        </div>
      </main>
          '''
    return output

if __name__ == "__main__":
    app.run(debug=True)
