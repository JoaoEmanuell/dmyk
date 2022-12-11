import android.app.NotificationManager;
import android.content.Context;
import android.support.v4.app.NotificationCompat;
import android.app.Activity;

public class ProgressBar {
    private NotificationManager mNotifyManager;
    private NotificationCompat.Builder mBuilder;
    @SuppressWarnings("deprecation")
    public static void set_progress(Activity pyActivity, Context pyContext, String title, String text, Integer max, Integer actual, Boolean infinity) {
        int id = 1;
        @SuppressWarnings("deprecation")
        NotificationManager mNotifyManager = (NotificationManager) pyContext.getSystemService(pyContext.NOTIFICATION_SERVICE);
        @SuppressWarnings("deprecation")
        NotificationCompat.Builder mBuilder = new NotificationCompat.Builder(pyActivity);
        mBuilder.setContentTitle(title)
                .setContentText(text)
                .setSmallIcon(pyContext.getApplicationInfo().icon);

        mBuilder.setProgress(max, actual, infinity);
        mNotifyManager.notify(id, mBuilder.build());
    }
}
