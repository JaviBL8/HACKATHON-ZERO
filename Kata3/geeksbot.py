from telegram.ext import CommandHandler, Updater


def main():
    updater = Updater(token="1133003116:AAH7Y3kisyOheA6qcL9fXKTiI8q-kWWSrD4", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repeat", repeat))
    updater.dispatcher.add_handler(CommandHandler("sum_numbers", sum_numbers))
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text("Hola soy un bot")


def repeat(update, context):
    update.message.reply_text(update.message.text)


def sum_numbers(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado es " + resultado)


main()
