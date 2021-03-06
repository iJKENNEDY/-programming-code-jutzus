package com.example.appcompatactivity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.GridView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private GridView gridview;
    private GridAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ArrayList<String> arrayList = new ArrayList<>();

        arrayList.add("Paola");
        arrayList.add("Fernando");
        arrayList.add("Alexander");
        arrayList.add("Melani");
        arrayList.add("Octavio");
        arrayList.add("Kenneth");
        arrayList.add("Karla");
        arrayList.add("Mirella");
        arrayList.add("Ricky");
        arrayList.add("Basil");
        arrayList.add("Rose");
        arrayList.add("Theresa");
        arrayList.add("Jose");
        arrayList.add("Jinne");
        arrayList.add("Washinton");


        gridview = (GridView) findViewById(R.id.an_gv_gridview);
        adapter = new GridAdapter(this,arrayList);
        gridview.setAdapter(adapter);

        gridview.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                Intent intent = new Intent(MainActivity.this, DetallesActivity.class);
                intent.putExtra("Nombre", adapter.getItem(position).toString());
                startActivity(intent);

            }
        });
    }
}