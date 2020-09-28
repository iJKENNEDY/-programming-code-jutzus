package com.example.ejemploadapter_ct1_s04;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //necesitamos armar la coleccion

        List<Pelicula> peliculas = ServicioPeliculas.consultarTodasLasPeliculas();
        //necesitamos el listView que representar las peliculas
        ListView lvPeliculas=(ListView)findViewById(R.id.lvPeliculas);
        //relacionar listView con el List<Peliculas>
        PeliculasArrayAdapter adapter = new PeliculasArrayAdapter(peliculas);
        lvPeliculas.setAdapter(adapter);

    }
}