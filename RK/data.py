from language import language
from mytool import tool
from LangTool import LangTool
#список средств разработки
tools = [tool(1,"Visual Studio"),
         tool(2,"Visual Studio Code"),
         tool(3, 'Android Studio')]
#список языков программирования
languages = [ language(1, 'Python', 1991, 1),
              language(2, 'C++', 1983, 2),
              language(3, 'Assembly', 1949, 3),
              language(4, 'Pascal', 1970, 2),
              language(5, 'Java', 1995, 1)]
#список связей многие-ко-многим
lang_tool = [
    LangTool(1, 1),
    LangTool(1, 2),
    LangTool(1, 3),
    LangTool(2, 2),
    LangTool(3, 4),
    LangTool(3, 5),

]
#связь один-ко-многим
one_to_many = [(l.title, l.year_app, t.name)
                   for t in tools
                   for l in languages
                   if l.tool_id == t.id]
#связь многие-ко-многим
many_to_many = [(l.title, l.year_app, t.name)
                    for t in tools
                    for l in languages
                    for relation in lang_tool
                    if t.id == relation.tool_id and l.id == relation.lang_id]
