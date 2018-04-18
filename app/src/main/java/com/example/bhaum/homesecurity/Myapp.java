package com.example.bhaum.homesecurity;

import android.app.Application;
import android.content.Context;
import android.widget.Toast;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.messaging.FirebaseMessaging;

/**
 * Created by bhaum on 09-03-2018.
 */

public class Myapp extends Application {

    public static FirebaseMessaging m;
    public static Context con;
    static FirebaseDatabase db;
    static DatabaseReference ref;

    @Override
    public void onCreate() {
        super.onCreate();
        con=getApplicationContext();
        m=FirebaseMessaging.getInstance();

        db=FirebaseDatabase.getInstance();
        ref=db.getReference();
        ref.child("token").setValue(FirebaseInstanceId.getInstance().getToken()+"");
        Toast.makeText(con, "Token : "+FirebaseInstanceId.getInstance().getToken()+"",Toast.LENGTH_LONG).show();
        m.subscribeToTopic("noti");

    }
}
