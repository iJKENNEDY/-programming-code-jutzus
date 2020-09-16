
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
    	msumTotalLabel.setText(sumOutput);
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
    }

    @Override
    protected void onStart(){
        super.onStart();
        Log.d(TAG, "onStart");
    }

    @Override
    protected void onRestart(){
        super.onRestart();
        Log.d(TAG, "onRestart");
    }

    @Override
    protected void onResume(){
        super.onResume();
        Log.d(TAG, "onResume");
    }

    @Override
    protected void onPause(){
        super.onPause();
        Log.d(TAG, "onPause");
    }

    @Override
    protected void onSaveInstanceState(Bundle outState){
        super.onSaveInstanceState(outState);
        Log.d(TAG, "onSaveInstanceState()");

        outState.putString(STATE_SUM_OUTPUT, sumOutput);
    }

    @Override
    protected void onStop(){
        super.onStop();
        Log.d(TAG, "onStop");
    }

    @Override
    protected void onDestroy(){
        super.onDestroy();
        Log.d(TAG, "onDestroy");
    }


    private void showRootScreen(){
        Intent intent= new Intent(this, RaizActivity.class);
        startActivity(intent);
    }

    private void addUserNumbers(){
        String inputA = mNumberAInput.getText().toString();
        String inputB = mNumberBInput.getText().toString();
        int numberA = inputA.isEmpty() ? 0: Integer.parseInt(inputA);
        int numberB = inputB.isEmpty() ? 0: Integer.parseInt(inputB);

        sumOutput = String.format(Locale.getDefault(), "= %d", numberA + numberB);
        msumTotalLabel.setText(sumOutput);
    }

}
