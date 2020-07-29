#lang slideshow
"wqert#"

(define circulo (circle 10))
(define rectangulo (rectangle 10 20))
rectangulo
circulo

"agregamos circulo y rectangulo"
(hc-append (circle 24)(rectangle 10 30))
(hc-append circulo rectangulo )

"diagramas con espacio"
(hc-append 20 circulo rectangulo circulo)

"local binding"
(define (four p)
  (define two-p(hc-append p p))
  (vc-append two-p two-p))
(four (circle 10))

"crear cuadrado"
(define (square n)
  ;este es un comentario
  (filled-rectangle n n))

"cuadrados 2x2"
(define (checker p1 p2)
  (let ([p12 (hc-append p1 p2)]
        [p21 (hc-append p2 p1)])
    (vc-append p12 p21)))
(checker (colorize (square 10) "red")
         (colorize (square 10) "black"))

"tabla de ajedrez"
(define (tableroAjedrez p)
  (let* ([rp (colorize p "red")]
         [bp (colorize p "black")]
         [c (checker rp bp)]
         [c4 (four c)])
    (four c4)))
(tableroAjedrez (square 10))