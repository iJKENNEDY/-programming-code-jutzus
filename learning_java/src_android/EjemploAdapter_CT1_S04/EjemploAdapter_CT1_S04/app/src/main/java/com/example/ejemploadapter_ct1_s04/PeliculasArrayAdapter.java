package com.example.ejemploadapter_ct1_s04;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.List;

public class PeliculasArrayAdapter extends BaseAdapter {

    private List<Pelicula> data;

    public PeliculasArrayAdapter(List<Pelicula> data) {this.data=data;}

    @Override
    public int getCount() {return data.size();}

    @Override
    public Object getItem(int position) {return data.get(position);}

    @Override
    public long getItemId(int position) {return position;}

    @Override
    public View getView(int position, View oldView, ViewGroup parent) {
        Pelicula pelicula = data.get(position);

        //queremos crear un view, siempre que oldview no este creado
        if (oldView==null) {
            LayoutInflater inflater= LayoutInflater.from(parent.getContext());
            oldView = inflater.inflate(R.layout.peliculas_list_item, parent, false);
            TextView tvTitulo = (TextView)oldView.findViewById(R.id.tvTitulo);
            TextView tvActores =(TextView)oldView.findViewById(R.id.tvActores);
            TextView tvFecha = (TextView)oldView.findViewById(R.id.tvFecha);

            PeliculasViewHolder peliculasViewHolder = new PeliculasViewHolder(tvTitulo, tvActores, tvFecha, pelicula);
            oldView.setTag(peliculasViewHolder);
        }else {
            ((PeliculasViewHolder)oldView.getTag()).bindItem(pelicula);
        }
        return oldView;
    }
}
