tema - bot | INFO: external_services.open_ai:msg = Message(id='msg_zlhj2KX8O1uzV2CwwmSsClzW', assistant_id=None, attachments=[], completed_at=None,
                                                           content=[TextContentBlock(text=Text(annotations=[], value='Создай картинку кота'),
                                                                                     type='text')], created_at=1716902561, incomplete_at=None,
                                                           incomplete_details=None, metadata={}, object='thread.message', role='user', run_id=None,
                                                           status=None, thread_id='thread_rfkm54F5kJopfQTVp1dBB139')
tema - bot | INFO: external_services.open_ai:msg = Message(id='msg_PYNn1ybjFcDZiHF1UBtqPKXR', assistant_id='asst_g6QLpRK271RzlicX6L55jwHE',
                                                           attachments=[], completed_at=None, content=[
        ImageFileContentBlock(image_file=ImageFile(file_id='file-ZksJQ0bATpnTzmGJtdxPx5Mk', detail=None), type='image_file'),
        TextContentBlock(text=Text(annotations=[], value='Вот простая картинка кота. Надеюсь, она вам понравится! 🐱'), type='text')],
                                                           created_at=1716902591, incomplete_at=None, incomplete_details=None, metadata={},
                                                           object='thread.message', role='assistant', run_id='run_AqwneD2THIdswzq56maV6tEX',
                                                           status=None, thread_id='thread_rfkm54F5kJopfQTVp1dBB139')
tema - bot | INFO: aiogram.event:Update
id = 776724870 is not handled.Duration
32468
ms
by
bot
id = 6601235729
tema - bot | ERROR: asyncio:Task
exception
was
never
retrieved
tema - bot | future: < Task
finished
name = 'Task-16'
coro = < BaseRequestHandler._background_feed_update()
done, defined
at / usr / local / lib / python3
.11 / site - packages / aiogram / webhook / aiohttp_server.py: 137 > exception = AttributeError(
    "'ImageFileContentBlock' object has no attribute 'text'") >
tema - bot | Traceback(most
recent
call
last):
tema - bot | File
"/usr/local/lib/python3.11/site-packages/pydantic/main.py", line
753, in __getattr__
tema - bot |
return pydantic_extra[item]
tema - bot | ~~~~~~~~~~~~~~ ^ ^ ^ ^ ^ ^
tema - bot | KeyError: 'text'
tema - bot |
tema - bot | The
above
exception
was
the
direct
cause
of
the
following
exception:
tema - bot |
tema - bot | Traceback(most
recent
call
last):
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/webhook/aiohttp_server.py", line
138, in _background_feed_update
tema - bot | result = await self.dispatcher.feed_raw_update(bot=bot, update=update, **self.data)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line
189, in feed_raw_update
tema - bot |
return await self.feed_update(bot=bot, update=parsed_update, **kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line
158, in feed_update
tema - bot | response = await self.update.wrap_outer_middleware(
    tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
                        tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/middlewares/error.py", line
25, in __call__
tema - bot |
return await handler(event, data)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/middlewares/user_context.py", line
27, in __call__
tema - bot |
return await handler(event, data)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/fsm/middleware.py", line
41, in __call__
tema - bot |
return await handler(event, data)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/app/middlewares/log_middleware.py", line
23, in __call__
tema - bot | result = await handler(event, data)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/event/telegram.py", line
121, in trigger
tema - bot |
return await wrapped_inner(event, kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/event/handler.py", line
43, in call
tema - bot |
return await wrapped()
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line
276, in _listen_update
tema - bot |
return await self.propagate_event(update_type=update_type, event=event, **kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
128, in propagate_event
tema - bot |
return await observer.wrap_outer_middleware(_wrapped, event=event, data=kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
123, in _wrapped
tema - bot |
return await self._propagate_event(
    tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
156, in _propagate_event
tema - bot | response = await router.propagate_event(update_type=update_type, event=event, **kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
128, in propagate_event
tema - bot |
return await observer.wrap_outer_middleware(_wrapped, event=event, data=kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
123, in _wrapped
tema - bot |
return await self._propagate_event(
    tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/old_router.py", line
148, in _propagate_event
tema - bot | response = await observer.trigger(event, **kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/event/telegram.py", line
121, in trigger
tema - bot |
return await wrapped_inner(event, kwargs)
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/event/handler.py", line
43, in call
tema - bot |
return await wrapped()
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/app/handlers/ai_questions.py", line
139, in ask_ai
tema - bot | await send_request(
    tema - bot | File
"/app/handlers/ai_questions.py", line
102, in send_request
tema - bot | response = await get_msg_response(
    tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
                        tema - bot | File
"/app/handlers/ai_questions.py", line
70, in get_msg_response
tema - bot |
return await thread_with_user.return_last_run_messages()
tema - bot | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
tema - bot | File
"/app/external_services/open_ai.py", line
243, in return_last_run_messages
tema - bot | _, value = c.text
tema - bot | ^ ^ ^ ^ ^ ^
tema - bot | File
"/usr/local/lib/python3.11/site-packages/pydantic/main.py", line
755, in __getattr__
tema - bot |
raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}') from exc
tema - bot | AttributeError: 'ImageFileContentBlock'
object
has
no
attribute
'text'
