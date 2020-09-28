package com.example.ejemploadapter_ct1_s04;

import java.util.Date;
import java.util.LinkedList;
import java.util.List;

public class ServicioPeliculas {
    public static List<Pelicula> consultarTodasLasPeliculas(){

        LinkedList<Pelicula> peliculas = new LinkedList<>();
        List<String> actores = new LinkedList<>();

        actores.add("Scarlet J.");
        peliculas.add(new Pelicula("Black R.", actores, new Date()));
        actores = new LinkedList<>();

        actores.add("Kenau Reves");
        peliculas.add(new Pelicula("Matrix", actores, new Date()));
        actores = new LinkedList<>();

        actores.add("Justin Timberlad");
        peliculas.add(new Pelicula("Red social", actores, new Date()));
        actores = new LinkedList<>();

        return peliculas;
    }
}
