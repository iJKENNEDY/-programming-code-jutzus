package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

public class sumaActivity extends AppCompatActivity {
    private static final String TAG = sumaActivity.class.getSimpleName();
    private static final String STATE_SUM_OUTPUT = "sumOutput";

    private EditText mNumberAInput;
    private EditText mNumberBInput;
    private TextView msumTotalLabel;
    private Button mAddButton;
    private Button mGetRootButton;

    private String sumOutput;
    
    protected void onCreate(Bundle savedInstanceState){
    	super.onCreate(savedInstanceState);
    	setContentView(R.layout.activity_suma);
    	Log.d(TAG, "onCreate()");
    	
    	//instancias
    	mNumberAInput= findViewById(R.id.number_a_imput);
    	mNumberBInput = findViewById(R.id.number_b_input);
    	msumTotalLabel=findViewById(R.id.sum_Label);
    	mAddButton= findViewById(R.id.add_button);
    	mGetRootButton = findViewById(R.id.get_root_button);

    	if (savedInstanceState != null) {
    		sumOutput = savedInstanceState.getString(STATE_SUM_OUTPUT);
    	}else{
    		sumOutput = "= 0";
    	}

    	///actualilzcion
    	msumTotalLabel.serText(sumOutput);
    	mAddButton.setOnClickListener(new View.OnClickListener() {
    		@Override
    		public void onClick(View v){
    			addUserNumbers();
    		}
    	});

    	mGetRootButton.setOnClickListener(new View.OnClickListener(){
    		@Override
    		public void onClick(View){
    			showRootScreen();
    		}
    	});
    	//pag_15
    }
}
