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


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        attr = {}
        if not attr:
            attr['stage'] = 1
        handler_input.attributes_manager.session_attributes = attr

        speak_output = "Hallo ich bin die weise Al Hexa. Ich besitze übernatürliche Kräfte und möchte sie dir zeigen. Vor Beginn unseres Abends habe ich eine Voraussage über die Spielkarte getroffen, die wir finden werden. Im Umschlag neben mir ist die Voraussage. Mein Assistent hat sechs Karten vor dich hingelegt und du wirst jetzt einmal würfeln. Ich werde meine übernatürlichen Kräfte sammeln und die Voraussage erfüllen. Sag mir bitte welche Zahl du gewürfelt hast."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


def getResolvedValue(request, slot_name):
    """Resolve the slot name from the request using resolutions."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return (request.intent.slots[slot_name].resolutions.
                resolutions_per_authority[0].values[0].value.name)
    except (AttributeError, ValueError, KeyError, IndexError, TypeError) as e:
        return None


def getAnswerFalse():
    """Wenn der Zuschauer etwas Falsches vorliest:"""
    return "Du Schelm. So eine Voraussage hab ich doch gar nicht getroffen. Unfug kannst du Sieri erzählen. Nicht mir. Ich glaube du solltest nochmal genauer lesen."


class AnweisungIntentHandler(AbstractRequestHandler):
    """Handler for AnweisungIntent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AnweisungIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        attr = handler_input.attributes_manager.session_attributes
        if (attr['stage'] == 1):

            augenzahl = getResolvedValue(handler_input.request_envelope.request, "augenzahl")

            if (augenzahl is not None):

                speak_output = "Glaubst du, dass das ein Zufall war? Mal sehen! "

                if (augenzahl.lower() == "eins"):
                    speak_output += "Drehe die Karte mit genau einem Symbol um. Schau dir anschließend die Rückseiten der anderen Karten an."
                elif (augenzahl.lower() == "zwei"):
                    speak_output += "Bewege die Spielfigur zwei Felder zu dir und drehe die Karte um. Schau dir anschließend die Rückseiten der anderen Karten an."
                elif (augenzahl.lower() == "drei"):
                    speak_output += "Bewege die Spielfigur drei Felder zu dir und drehe die Karte um. Schau dir anschließend die Bildseiten der anderen Karten an."
                elif (augenzahl.lower() == "vier"):
                    speak_output += "Schau dir die Bildseite der von dir aus vierten Karte an. Schau dir anschließend die Bildseiten der anderen Karten an."
                elif (augenzahl.lower() == "fünf"):
                    speak_output += "Schau dir die Rückseite der von dir aus fünften Karte an. Schau dir anschließend die Rückseiten der anderen Karten an."
                else:
                    speak_output += "Drehe bitte alle sechs Karten mit der Bildseite nach oben."

                speak_output += " Schau nun in den Umschlag neben mir. <break time='5s'/>Und lies meine Voraussage laut vor!"

                attr['stage'] += 1
                handler_input.attributes_manager.session_attributes = attr

                return (
                    handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
                )

            else:
                speak_output = "Du Schelm. Diese Zahl kannst du gar nicht gewürfelt haben. Sag mir was du wirklich gewürfelt hast."

                return (
                    handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
                )
        else:
            speak_output = getAnswerFalse()

            return (
                handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )


class EndeIntentHandler(AbstractRequestHandler):
    """Handler for AnweisungIntent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EndeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = "Tja, da hab ich dich wohl mit meinen übernatürlichen Kräften überrascht. Ich bin schließlich die wundervolle Al Hexa! Danke fürs Spielen."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = "Hallo ich bin die weise Al Hexa. Ich besitze übernatürliche Kräfte und möchte sie dir zeigen."

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
        speak_output = "Vielen Dank fürs Spielen!"

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

        attr = handler_input.attributes_manager.session_attributes
        if (attr['stage'] == 1):

            speak_output = "Ich hab deine Augenzahl nicht ganz verstanden. Kannst du sie nochmal wiederholen?"

            return (
                handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )

        elif (attr['stage'] == 2):

            speak_output = getAnswerFalse()

            return (
                handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
            )

        else:
            logger.info("In FallbackIntentHandler")
            speech = "Das habe ich nicht verstanden. Womit kann ich dir helfen?"
            reprompt = "Das habe ich nicht verstanden. Womit kann ich dir helfen?"

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

        speak_output = "Tut mir leid, ich hatte Probleme, dich zu verstehen. Kannst du das wiederholen?"

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

sb.add_request_handler(AnweisungIntentHandler())
sb.add_request_handler(EndeIntentHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler())  # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()