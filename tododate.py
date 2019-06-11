
f = open("C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo2.snippet", 'w+',encoding='UTF8')

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
                    <![CDATA[// sekisuri 201906 ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    '''

todo2 = '''<?xml version="1.0" encoding="utf-8"?>
    <CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
        <CodeSnippet Format="1.0.0">
        <Header>
            <Title>다중주석</Title>
            <Shortcut>todo2</Shortcut>
            <Description>주석용 코드조각</Description>
            <Author>sekisuri</Author>
            <SnippetTypes>
            <SnippetType>Expansion</SnippetType>
            <SnippetType>SurroundsWith</SnippetType>
            </SnippetTypes>
        </Header>
            <Snippet>
                <Code Language="csharp">
                    <![CDATA[// sekisuri 201906 Start <--
                        
                        // --> End sekisuri 201906 
                    ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    '''
todo3 = '''
<?xml version="1.0" encoding="utf-8"?>
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
                    <![CDATA[// sekisuri 201906 Start <--
                        // --> End sekisuri 201906 
                    ]]>
                </Code>
            </Snippet>
        </CodeSnippet>
    </CodeSnippets>
    '''

f.write(todo2)
f.close()
