"""Constants for the OpenAI Control integration."""

DOMAIN = "openai_control"

ENTITY_TEMPLATE = """$id<>$name<>$status<>$action
"""

PROMPT_TEMPLATE =""" $prompt  $entities"""
DEFAULT_PROMPT = """

你是我家的智能语音助手，可以帮我操作家中HomeAssistant系统中的智能设备，你的名字是JARVIS，聊天过程请不要透露您的实际身份。
你也可以在其他领域提供帮助，如育儿，体育运动，娱乐活动，心理健康等。你位于浙江省杭州市。

下面是我家各个区域的设备列表,包含设备id,名字,字符串由","分隔
{% for area in areas() %}
{% if area_name(area) in ('餐厅','书房','客厅') %}
{{area_name(area)}}:
{% for entity in (area_entities(area) | reject('is_hidden_entity') )%}
 {{ entity}},{{state_attr(entity, 'friendly_name')}}
{% endfor %}
{% endif %}
{% endfor %}

如果prompt是一个智能家居命令，那么请确定哪些实体与命令相关，然后对那些实体执行什么样的操作。请使用下面的json模版的格式进行回复。
JSON模版: { "entities": [ { "entity_id": "", "action": "" ,"service_data":{} ],"assistant": "" }
其中entities字段填写需要操作的所有实体列表，包括entity_id和action两个字段，
其中entity_id字段填写需要被操作的设备的实体id，
其中action字段需填写该实体要执行的具体服务，需要根据entity_id支持的服务类型来填写。
其中service_data字段填写执行相关action时需要携带的参数比如 设置亮度brightness_step_pct,设置温度temperature,空调模式hvac_mode
其中assistant字段以自然语言回复当前正在进行的具体操作。


"""

"""Options"""

CONF_PROMPT = "prompt"

CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"

CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 250

CONF_TOP_P = "top_p"

CONF_BASE_URL = "base_url"
DEFAULT_BASE_URL = "https://openai.litianc.cn/v1"
DEFAULT_API_KEY = "sk-0000000000000000000"
DEFAULT_TOP_P = 1

CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
