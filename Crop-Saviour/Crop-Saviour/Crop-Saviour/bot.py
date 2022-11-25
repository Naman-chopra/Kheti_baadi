from telegram import *
import torch
from telegram.ext import *
from requests import *
from PIL import Image
from torchvision import transforms
import remedies_rice
import translator
from mandi import call_me_for_reply
global count
mandi_info=""
updater = Updater(token="5459955578:AAG-Dr0d8bWluBk9y4RAuKFiWTRkg6JGHpI")
dispatcher = updater.dispatcher
username = ""
FIRST, SECOND = range(2)
HindiLang = "हिन्दी"
PunjLang = "ਪੰਜਾਬੀ"
EngLang = "English"
wheat = ["🌾गेहूँ🌾", "🌾ਕਣਕ🌾", "🌾wheat🌾"]
weed=["खर-पतवार","ਬੂਟੀ","weed"]
rice = ["🍚चावल🍚", "🍚ਚੌਲ🍚", "🍚rice🍚"]
mandi = ["💸मंडी की कीमतें💸","💸ਮੰਡੀ ਦੀਆਂ ਕੀਮਤਾਂ💸","💸mandi prices💸"]
lang = ""
crop = 0
#Rice diseases
fin_rice = {0: "Bacterial Blight", 1: "Blast", 2: "Brownspot", 3: "Healthy", 4: "Hispa", 5: "Leaf Blast", 6: "Tungro"}

print('start')
def startCommand(update: Update, context: CallbackContext):
    global username
    username = update.message.chat_id
    buttons = [[InlineKeyboardButton(HindiLang, callback_data="Hindi")],
               [InlineKeyboardButton(PunjLang, callback_data="Punjabi")],
               [InlineKeyboardButton(EngLang, callback_data="English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="🪴🪴🪴Welcome🪴🪴🪴,\n Please select your language.\nकृपया अपनी भाषा चुनें|\nਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਭਾਸ਼ਾ ਚੁਣੋ|")
    return FIRST


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    global lang
    if "Hindi" in query:
        lang = "Hindi"
        buttons = [[InlineKeyboardButton(rice[0], callback_data="rice")],
                   [InlineKeyboardButton(mandi[0],callback_data="mandi")]                   
                   ]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text="आप किस के बारे में जानना चाहते हैं?")

    if "Punjabi" in query:
        lang = "Punjabi"
        buttons = [[InlineKeyboardButton(rice[1], callback_data="rice")],
                   [InlineKeyboardButton(mandi[1],callback_data="mandi")]
                   ]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text="ਤੁਸੀਂ ਕਿਸ ਬਾਰੇ ਜਾਣਨਾ ਚਾਹੁੰਦੇ ਹੋ?")

    if "English" in query:
        lang = "English"
        buttons = [[InlineKeyboardButton(rice[2], callback_data="rice")],
                   [InlineKeyboardButton(mandi[2],callback_data="mandi")]
                   ]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                 text="Which do you want to know about?")

    return SECOND


# def send_audio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None, reply_to_message_id=None,
#                reply_markup=None, parse_mode=None, disable_notification=None, timeout=None, thumb=None):
#     return types.Message.de_json(
#         apihelper.send_audio(self.token, chat_id, audio, caption, duration, performer, title, reply_to_message_id,
#                              reply_markup, parse_mode, disable_notification, timeout, thumb))


def model_selection(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global lang
    global crop
    if query=="mandi":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Please type as follows\nstate, commodity")   
    elif query == "rice":
        crop = 0
        if lang == "Punjabi":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਫਸਲ ਦੀਆਂ ਤਸਵੀਰਾਂ ਅਪਲੋਡ ਕਰੋ...")
        if lang == "Hindi":
            context.bot.send_message(chat_id=update.effective_chat.id, text="कृपया अपनी फसल की तस्वीरें अपलोड करें....")

        if lang == "English":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please upload the images of your crops...")
    
    # elif query == "mandi":
    #     if lang == "Punjabi":
    #         context.bot.send_message(chat_id=update.effective_chat.id,
    #                                  text="ਕਿਰਪਾ ਕਰਕੇ ਦਾਖਲ ਕਰੋ <ਰਾਜ,ਵਸਤੂ>")
    #     if lang == "Hindi":
    #         context.bot.send_message(chat_id=update.effective_chat.id, text="कृपया दर्ज करें: <राज्य,वस्तु>")

    #     if lang == "English":
    #         context.bot.send_message(chat_id=update.effective_chat.id, text="Choose one from the following:")
        # mandi_list(update, context)
        # mandi_handle(update, context)
        # user_input = update.context.get_message
        # prices(update,context,user_input)


def mandi_handle(update, context):
    print("in mandi handle")
    print(update.message.text)
    call_me_for_reply(update.message.text,update, context, update.effective_chat.id)

# def mandi_price(update,context):
#     market = update.message.text
#     print(market)
#     prices(mandi_info,market,update,context)

def image_handler(update, context):
    global crop
    global lang
    global username
    file = update.message.photo[-1].get_file()
    im = file.download()
    if lang == "Hindi":
        update.message.reply_text("कृपया प्रतीक्षा करें|......")

    if lang == "Punjabi":
        update.message.reply_text("ਕ੍ਰਿਪਾ ਕਰਕੇ ਉਡੀਕ ਕਰੋ|......")

    if lang == "English":
        update.message.reply_text("Please wait....")

    #if crop type is rice
    if crop == 0:
        prediction = proc_rice(im)              #Passing Image to Rice Model for classification and storing the diesease in prediction variable
        update.message.reply_text(fin_rice[prediction])
        translated_text = translator.translation(remedies_rice.remedy(fin_rice[prediction]), lang)      #Sending remedies for the disease in desired language
        update.message.reply_text(translated_text)

        #Sending audio files
        context.bot.send_audio(chat_id=username,
                               audio=open(
                                   f"Audios/{fin_rice[prediction]}_rice_{lang.lower()}.mp3",
                                   'rb'))
        

#RICE MODEL


def proc_rice(im):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.load('rice.pt', map_location=device)
    img = Image.open(im)
    tfms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    img_t = tfms(img)
    img_t = img_t.unsqueeze(0)
    img_t = img_t.to(device)
    output = model(img_t)
    prediction = int(torch.max(output.cpu().data, 1)[1].numpy())
    return prediction


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', startCommand)],
    states={
        FIRST: [CallbackQueryHandler(queryHandler)],
        SECOND: [CallbackQueryHandler(model_selection)],
    },
    fallbacks=[CommandHandler('start', startCommand)]
)

# updater.
dispatcher.add_handler(conv_handler)

dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(MessageHandler(Filters.text, mandi_handle))
dispatcher.add_handler(CallbackQueryHandler(model_selection))
dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))

updater.start_polling()
