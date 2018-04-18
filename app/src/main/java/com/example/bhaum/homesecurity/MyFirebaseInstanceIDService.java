package com.example.bhaum.homesecurity;

import android.util.Log;
import android.widget.Toast;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

/**
 * Created by Meet on 29-08-2017.
 */

public class MyFirebaseInstanceIDService extends FirebaseInstanceIdService {
    @Override
    public void onTokenRefresh() {
        // Get updated InstanceID token.
        String refreshedToken = FirebaseInstanceId.getInstance().getToken();
        Log.d("Token", "Refreshed token: " + refreshedToken);


        Toast.makeText(Myapp.con,"new token : "+refreshedToken,Toast.LENGTH_LONG).show();
        // If you want to send messages to this application instance or
        // manage this apps subscriptions on the server side, send the
        // Instance ID token to your app server.
        sendRegistrationToServer(refreshedToken);
    }
    private void sendRegistrationToServer(String token) {

        Toast.makeText(Myapp.con,"token : "+token,Toast.LENGTH_LONG).show();
// TODO: Implement this method to send token to your app server.
    }
}
