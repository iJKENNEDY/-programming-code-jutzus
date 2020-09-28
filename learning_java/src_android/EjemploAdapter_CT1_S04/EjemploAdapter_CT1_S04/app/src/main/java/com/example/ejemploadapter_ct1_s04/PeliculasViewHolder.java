package com.example.ejemploadapter_ct1_s04;

import android.widget.TextView;

public class PeliculasViewHolder {
    private TextView tvTitulo;
    private TextView  tvActores;
    private TextView  tvFecha;
    private Pelicula item;

    public PeliculasViewHolder(TextView tvTitulo,
                               TextView tvActores,
                               TextView tvFecha,
                               Pelicula item) {
        this.tvActores = tvActores;
        this.tvFecha = tvFecha;
        this.tvTitulo = tvTitulo;
        bindItem(item);
    }

    //nos permite cuando reutilizamos el View, modificar el dato al que se hace referencia
    public void bindItem(Pelicula item) {
        this.item = item;
        tvTitulo.setText(item.getTitulo());
        tvActores.setText(item.getActores().toString());
        tvFecha.setText(item.getFechaEstreno().toString());
    }
}
