from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

adMetrics = SimpleRouter();

urlpatterns = [
    path("", views.index, name="index"),
    path('metrics/', views.ad_tracking_metrics, name='ad_tracking_metrics'),
    path('ad-impression', views.TODO_AD_IMPRESSION_VIEW , name=""),
    path('ad-click', views.TODO_AD_CLICK_VIEW , name=""),
]

'''
In Option 1, step 3, the Frontend will need to send data to the backend. This is
most safely done with a beacon.
https://developer.mozilla.org/en-US/docs/Web/API/Beacon_API

Similarly, to log a click, you will need to send a beacion in the click event
handler for the ad. Rather than navigating on click, you will need to use
JavaScript to intercept the client event, cancel the default event, send a
beacon, then trigger navigation. The end result should be that the click is
logged and the end user experience is identical to a normal link click.

For example:

// Prefered style - does not inturrupt flow of web navigation
link.addeEventListner((event) => {
    navigator.beacon(CLICK_URL, {ad_id: "AD ID"});
})

// Older style - assumes link target is an anchor tag (<a>)
link.addeEventListner(async (event) => {
    event.preventDefault();
    await fetch(CLICK_URL, {ad_id: "AD ID"});
    window.location = event.target.href;
})

The above code is plain JavaScript. The idea shown above will need to be adapted
to React.

---

* Repo 1 - Backend
* Repo 2 - Frontend

**Option 1 - Event sequence** 0. User navigates to an AMO page, requesting a
HTML page from frontend server. 1. Frontend servers the page. During load,
randomly selects an Ad to show (`AdID`). 2. Frontend posts a message to Backend
to log dispaly of `AdID`.
    POST {adid: "my-ad"}
3. Backend recieves API request to log display of `AdID`.
4. Backend API (view|modle|something) updates database to increment ad view
   count.

Option 2 - Event sequence 0. User navigates to an AMO page, requesting a HTML
page from frontend server. 1. Backend serves the page. During load randomly
selects an Ad to show (`AdID`). 2. As part of serving the requested page,
backend updates database to increment ad view count.


http://olympia.test:3333/ads/pocket.html http://olympia.test:3333/
    - This also contains all ads

'''