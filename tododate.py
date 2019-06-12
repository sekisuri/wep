import argparse
from datetime import datetime

now = datetime.now()
ftodo1 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo.snippet" 
ftodo2 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo2.snippet"
ftodo3 = "C:\\Users\\wizar\\OneDrive\\문서\\MySnippet\\myTodo3.snippet"  


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
             </SnippetTypes>
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

def main():
    parser = argparse.ArgumentParser()
    parser .add_argument("op",type=str,
    choices=['todo1','todo2','todo3','all'],
    help="choice todo1 , todo2 , todo3 , all")
    args = parser.parse_args()
    opstr = args.op
    makerun(opstr)
   

def makerun(op):
    if op == 'todo1':
        f = open(ftodo1,"w+",encoding="utf-8")
        f.write(todo1)
        f.close()
    elif op == 'todo2':
        f = open(ftodo2,"w+",encoding="utf-8")
        f.write(todo2)
        f.close()
    elif op == 'todo3':
        f = open(ftodo3,"w+",encoding="utf-8")
        f.write(todo3)
        f.close()
    elif op == 'all':
        f1 = open(ftodo1,"w+",encoding="utf-8")
        f1.write(todo1)
        f1.close()
        f2 = open(ftodo2,"w+",encoding="utf-8")
        f2.write(todo2)
        f2.close()
        f3 = open(ftodo3,"w+",encoding="utf-8")
        f3.write(todo3)
        f3.close()
    else :
        print("arg error")

#test
if __name__=="__main__":
    main()

