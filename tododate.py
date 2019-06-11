from datetime import datetime

now = datetime.now()
ftodo1 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo.snippet" 
ftodo2 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo2.snippet"
ftodo3 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo3.snippet"  

f = open(ftodo2, 'w+',encoding='UTF8')

settime = "%s-%s-%s" %(now.year,now.month,now.day)
todo1 = '''<?xml version="1.0" encoding="utf-8"?>
    <CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
        <CodeSnippet Format="1.0.0">
        <Header>
            <Title>단일주석</Title>
            <Shortcut>todo1</Shortcut>
            <Description>단일주석용 코드조각</Description>
            <Author>sekisuri</Author>
            <SnippetTypes>
            <SnippetType>Expansion</SnippetType>
            <SnippetType>SurroundsWith</SnippetType>
            </SnippetTypes>
        </Header>
            <Snippet>
                <Code Language="csharp">
                    <![CDATA[// sekisuri %s ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    ''' % settime

todo2 = '''<?xml version="1.0" encoding="utf-8"?>
    <CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
        <CodeSnippet Format="1.0.0">
        <Header>
            <Title>다중주석</Title>
            <Shortcut>todo2</Shortcut>
            <Description>다중주석용 코드조각</Description>
            <Author>sekisuri</Author>
            <SnippetTypes>
            <SnippetType>Expansion</SnippetType>
            <SnippetType>SurroundsWith</SnippetType>
            </SnippetTypes>
        </Header>
            <Snippet>
                <Code Language="csharp">
                    <![CDATA[// sekisuri %s Start <--
                        
                        // --> End sekisuri  
                    ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    ''' % settime
todo3 = '''<?xml version="1.0" encoding="utf-8"?>
    <CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
        <CodeSnippet Format="1.0.0">
        <Header>
            <Title>클래스 설명</Title>
            <Shortcut>todo3</Shortcut>
            <Description>클래서 설명 주석</Description>
            <Author>sekisuri</Author>
            <SnippetTypes>
            <SnippetType>Expansion</SnippetType>
            <SnippetType>SurroundsWith</SnippetType>
        </Header>
            <Snippet>
                <Code Language="csharp">
                    <![CDATA[
                    /*
                    Author : sekisuri
                    Date : %s
                    */
                    ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    ''' % settime

#f.write(todo2)
print(settime)
f.close()
