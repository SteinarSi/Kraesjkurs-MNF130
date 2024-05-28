# Kræsjkurs MNF130

Her er presentasjonen og kildekoden til et kræsjkurs i MNF130, som har blitt brukt i årene 2022-2024. 

### Presentasjonen
Den korte versjonen er `Kræsjkurs.pdf`.

Den lange versjonen, med et nytt lysbilde for hver ting som skal dukke opp underveis, er `Kræææsjkurs.pdf`.

Merk at noen av temaene vi har lysbilder på ikke er pensum i 2024. Likevel har vi beholdt lysbildene for de temaene, siden det er høyst sannsynlig at det er en annen emneansvarlig neste år og at noen av temaene kommer tilbake. Det gjelder:
* Strukturell induksjon
* Relasjoner
* Tellbarhet
* Kryptografi
* Trær

### Opptaket
https://www.youtube.com/watch?v=Yg5BX6h-4y4 

### Kildekoden
Om du skal holde ditt eget kræsjkurs, og vil ta utgangspunkt i dette, må du gjerne gjøre det. Bare husk å ha med lisensen nedenfor. Du kan generere presentasjonen ved å kompilere `main.tex`, for eksempel med en kommando som `pdflatex -shell-escape main.tex`. Det tar noen minutter, så når du jobber med lysbildene anbefales det å kommentere ut kapitlene du ikke jobber med. For å bytte mellom å generere et nytt lysbilde for hver `\pause`, og å ikke gjøre det, kan du fjerne eller legge til nøkkelordet `handout` øverst i `main.tex`.

***

### License
Copyright 2024 Steinar Simonnes

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
