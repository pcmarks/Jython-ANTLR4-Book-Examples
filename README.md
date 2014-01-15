
Jython Versions of the ANTLR4 Book Examples
===========================================

This repository contains Jython translations of some of the ANTLR4 examples found in the book "The Definitive
ANTLR4 Reference" by Terrance Parr. The original, java examples can
be downloaded from: http://pragprog.com/titles/tpantlr2/source_code

Setup
-----
The following steps assume:
 * jython is in your system's execution path - Jython 2.7b1 was used.
 * The ANTLR v4 library (jar file) is in the CLASSPATH.
 * a4 command invokes the ANTLR v4 Tool.

Typical Steps
-------------
 1. a4 Grammar.g4
 2. javac Grammar*.java
 3. jython example.py test_file

Specific Steps
--------------
tour/Calc.py
 1. a4 -no-listener -visitor LabeledExpr.g4
 2. javac LabeledExpr*.java
 3. jython Calc.py t.expr

tour/ExtractInterfaceTool.py
 1. a4 Java.g4
 2. javac Java*.java
 3. jython ExtractInterfaceTool.py Demo.java

tour/Col.py
 1. a4 -no-listener Rows.g4
 2. javac Rows*.java
 3. jython Col.py 1 t.rows
 4. jython Col.py 2 t.rows
 5. jython Col.py 3 t.rows

tour/InsertSerialID.py
 1. a4 Java.g4
 2. javac Java*.java
 3. jython InsertSerialID.py Demo.java

listeners/TestPropertyFile.py
 1. a4 PropertyFile.g4
 2. javac PropertyFile*.java
 3. jython TestPropertyFile.py t.properties

listeners/TestPropertyFileVisitor.py
 1. a4 -visitor PropertyFile.g4
 2. javac PropertyFile*.java
 3. jython TestPropertyFileVisitor.py t.properties

listeners/TestEvaluator.py
 1. a4 Expr.g4
 2. javac Expr*.java
 3. jython TestEvaluator.py t.expr

listeners/LoadCSV.py
 1. a4 CSV.g4
 2. javac CSV*.java
 3. jython LoadCSV.py t.csv

listeners/CallGraph.py
 1. a4 Cymbol.g4
 2. javac Cymbol*.java
 3. jython CallGraph.py t.cymbol > CallGraph.dot
 4. dot -Tpng CallGraph.dot -o CallGraph.png        (*nix Graphviz)
