# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#--------------------start own code--------------------------------
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        
        attr = {}
        if not attr:
            attr['state'] = 'START'
            attr['stop'] = 'NULL'
            
            attr['herzartig'] = 'NULL'
            attr['farbe'] = 'NULL'
            attr['wert'] = 'NULL'

            attr['name'] = 'NULL'
            attr['glauben'] = 'NULL'
            
        handler_input.attributes_manager.session_attributes = attr

        return (
            handler_input.response_builder
                .speak('Hallo, ich bin Al Hexa, die große Zauberkünstlerin. Mein Assistent hat ein Kartenspiel. <break time="2s"/> Er legt jetzt eine Karte nach der anderen auf den Tisch. <break time="3s"/> Wenn du eine Karte wählen willst, tippe mit einen Finger darauf und sage fertig. Achtung, ab jetzt sage kein Wort, dass mir diese Karte verraten könnte.')
                .ask('Wenn du bereit bist, dann sage fertig.')
                .response
        )

def main(string_value, handler_input):
    attr = handler_input.attributes_manager.session_attributes
    state = attr['state']
    if state == 'START':
        if string_value == 'fertig':
            state = 'WAHL_KARTE'
            attr['state'] = state
            handler_input.attributes_manager.session_attributes = attr
            return 'Kennst du die Karte, die Du gewählt hast?'
        return 'Wenn du bereit bist, dann sage fertig.'
    elif state == 'WAHL_KARTE':
        if string_value == 'Ja':
            attr['state'] = 'HERZARTIG'
            attr['herzartig'] = 'Ja'
            handler_input.attributes_manager.session_attributes = attr
            return 'Merke sie dir gut und konzentriere dich auf deine Karte. Versuche sie mir mittels Gedankenströmen zu übermitteln! <break time="2s"/> Sage fertig, wenn du dir die Karte gut eingeprägt hast.'
        elif string_value == 'Nein':
            attr['state'] = 'HERZARTIG'
            attr['herzartig'] = 'Nein'
            handler_input.attributes_manager.session_attributes = attr
            return 'Das ist auch völlig unmöglich, da du sie nicht sehen kannst. Es ist auch völlig unmöglich, dass ich die Karte kenne, denn ich kann sie auch nicht sehen. Aber du kannst sie mir durch Gedankenströme übermitteln. Sieh sie dir genau an und konzentriere dich. <break time="3s"/> Sage fertig, wenn du dir die Karte gut eingeprägt hast.'
        return 'Kennst du die Karte, die Du gewählt hast?'
    elif state == 'HERZARTIG':
        if string_value == 'fertig':
            attr['state'] = 'NAME'
            handler_input.attributes_manager.session_attributes = attr
            return 'Ich habe dich noch gar nicht nach deinem Namen gefragt. Ich bin Al Hexa, die große Zauberkünstlerin. Und wie heißt du.'
        return 'Sage fertig, wenn du dir die Karte gut eingeprägt hast.'
    elif state == 'NAME':
        attr['state'] = 'GEDANKEN'
        attr['name'] = string_value
        handler_input.attributes_manager.session_attributes = attr
        return '' + string_value + ', glaubst du, dass du es schaffst, deine Karte durch Gedankenströme an mich zu übermitteln?'
    elif state == 'GEDANKEN':
        a = 'Ich versuche deine Gedanken zu lesen. <break time="3s"/> Nun bisher kommt bei mir noch nichts an. Erkennst du das Bild auf der Vorderseite deiner Karte klar und deutlich?'
        if string_value == 'Ja':
            attr['glauben'] = ''
            attr['state'] = 'GEDANKEN_2'
            handler_input.attributes_manager.session_attributes = attr
            return 'Sehr gut, wenn du daran glaubst, dann schaffst du es auch. Lass uns beginnen! ' + a
        #elif string_value == 'Nein' or string_value is undefined:
        attr['state'] = 'GEDANKEN_2'
        attr['glauben'] = ' nicht '
        handler_input.attributes_manager.session_attributes = attr
        return 'Kann ich verstehen. Aber gib mir trotzdem eine Chance und spiele bitte mit. Lass uns beginnen! ' + a
    elif state == 'GEDANKEN_2':
        a = '<break time="3s"/> Ich versuche es weiter. Lass dich bitte nicht in deiner Konzentration stören. <break time="3s"/> Irgendwie kommen noch keine Gedankenströme an. Hältst du die Karte in der Hand?'
        if string_value == 'Ja':
            attr['state'] = 'GEDANKEN_3'
            attr['farbe'] = 'rote'
            handler_input.attributes_manager.session_attributes = attr
            return 'Lasse deine Augen nicht von der Karte und konzentriere dich darauf!' + a
        elif string_value == 'Nein':
            attr['state'] = 'GEDANKEN_3'
            attr['farbe'] = 'schwarze'
            handler_input.attributes_manager.session_attributes = attr
            return 'Dann muss ich mich auch nicht wundern. <break time="2s"/> Versuchen wir es noch einmal. Konzentration bitte.' + a
        return 'Kannst du dein Kartenbild gut sehen?'
    elif state == 'GEDANKEN_3':
        name = attr['name']
        a = '<break time="3s"/> Ja. Ich kann jetzt etwas empfangen. Ja, so langsam erscheinen Bilder in meinem elektronischen Gehirn. ' + name + ', Glaubst du immer noch'+attr['glauben']+', dass uns das Experiment gelingt?'
        if string_value == 'Ja':
            attr['state'] = 'GEDANKEN_4'
            attr['wert'] = 'hoher'
            handler_input.attributes_manager.session_attributes = attr
            return 'Dann achte bitte darauf, dass deine Finger nichts verdecken. Du musst das vollständige Bild sehen können, damit du mir die Karte übertragen kannst. Bitte konzentrieren!' + a
        elif string_value == 'Nein':
            attr['state'] = 'GEDANKEN_4'
            attr['wert'] = 'niedriger'
            handler_input.attributes_manager.session_attributes = attr
            return 'Bitte nimm sie in die Hand, ganz nahe zu dir. Wir versuchen es noch einmal. Bitte konzentrieren!' + a
        return 'Hältst du die Karte in der Hand?'
    elif state == 'GEDANKEN_4':
        attr['state'] = 'KARTE_ERRATEN'
        handler_input.attributes_manager.session_attributes = attr
        return 'Du wirst sehen, ich schaffe das. Bitte konzentriere dich. Am besten, du hältst die Karte noch näher zu dir. Ja, die Bilder werden deutlicher. Sprich jetzt bitte kein Wort, aber konzentriere dich weiter. ' + calcCard(handler_input)
    elif state == 'KARTE_ERRATEN':
        if string_value == 'Ja':
            attr['state'] = 'KARTE_ERRATEN_JA'
            attr['stop'] = 'YES'
            handler_input.attributes_manager.session_attributes = attr
            return 'Ich wusste es doch, ich kann deine Gedanken erraten. Ja, jetzt auch. Aber keine Angst, ich sage es keinem weiter. ' + attr['name'] + ' Vielen Dank fürs Mitmachen.'
        elif string_value == 'Nein':
            attr['state'] = 'KARTE_ERRATEN_NEIN'
            attr['stop'] = 'YES'
            handler_input.attributes_manager.session_attributes = attr
            return 'Schade, dass muss daran liegen, dass hier so viele andere Leute mit ihren Gedanken dazwischendenken. Aber trotzdem' + attr['name'] + 'vielen Dank fürs Mitmachen, '  + '.'
        return calcCard(handler_input)
    return 'Error'



def calcCard(handler_input):
    attr = handler_input.attributes_manager.session_attributes
    wert = attr['wert']
    farbe = attr['farbe']
    herzartig = attr['herzartig']
    n = 0
    response = ''
    
    if wert == 'NULL' or farbe == 'NULL' or herzartig == 'NULL':
        return 'Error'
    
    if wert == 'niedriger':
        n += 1
    
    if farbe == 'schwarze':
        n += 2
        response = 'Ich sehe eine schwarze Karte, <break time="1s"/> '
    else:
        response = 'Ich sehe eine rote Karte, <break time="1s"/> '
    
    if herzartig == 'Ja':
        n += 4
    
    mapping = {
        0: 'und eine Frau mit einer Blume in der Hand. Das bedeutet, es ist <break time="1s"/> die Karo Dame, oder?',
        1: 'und ein paar Vierecke darauf. Das bedeutet, es ist <break time="1s"/> die Karo 5, oder?',
        2: 'und einen Mann mit einem Schwert in der Hand. Das bedeutet, es ist <break time="1s"/> der Kreuz König, oder?',
        3: 'und ein paar Kreuze darauf. Das bedeutet, es ist <break time="1s"/> die Kreuz 6, oder?',
        4: 'und viele Herzen darauf. Das bedeutet, es ist <break time="1s"/> die Herz 10, oder?',
        5: 'und ein paar Herzen darauf. Das bedeutet, es ist <break time="1s"/> die Herz 6, oder?',
        6: 'und viele Blätter darauf. Das bedeutet, es ist <break time="1s"/> die Pik 9, oder?',
        7: 'und ein paar Blätter darauf. Das bedeutet, es ist <break time="1s"/> die Pik 3, oder?'
    }
    
    return response + mapping[n]


class ConfirmationIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ConfirmationIntent")(handler_input)
    def handle(self, handler_input):
        str = main('fertig', handler_input)
        return (
            handler_input.response_builder
            .speak(str)
            .ask(str)
            .response
        )
class YesIntetntHandler(AbstractRequestHandler):
    """Handler for Yes Intent"""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)
    
    def handle(self, handler_input):
        str = main('Ja', handler_input)
        attr = handler_input.attributes_manager.session_attributes
        if(attr['stop']=='YES'):
            return (
             handler_input.response_builder
            .speak(str)
            .response   
            )
        return (
            handler_input.response_builder
            .speak(str)
            .ask(str)
            .response
        )

class NoIntetntHandler(AbstractRequestHandler):
    """Handler for Yes Intent"""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)
    
    def handle(self, handler_input):
        str = main('Nein', handler_input)
        attr = handler_input.attributes_manager.session_attributes
        if(attr['stop']=='YES'):
            return (
             handler_input.response_builder
            .speak(str)
            .response   
            )
        return (
            handler_input.response_builder
            .speak(str)
            .ask(str)
            .response
        )

class NameIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NameIntent")(handler_input)
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        name = slots['name'].value
        str = main(name, handler_input)
        return (
            handler_input.response_builder
            .speak(str)
            .ask(str)
            .response
        )

#--------------------end own code--------------------------------




class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = main('Hilfe', handler_input)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Danke für's Spielen!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = main('Fallback', handler_input)
        reprompt = speech

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = main('Error', handler_input)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_request_handler(ConfirmationIntent())
sb.add_request_handler(YesIntetntHandler())
sb.add_request_handler(NoIntetntHandler())
sb.add_request_handler(NameIntent())

sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()