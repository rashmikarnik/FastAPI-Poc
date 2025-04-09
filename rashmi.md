# - name: install the gcloud cli
      #   uses: google-github-actions/setup-gcloud@v1
      #   with:
      #     service_account_key: ${{ secrets.GOOGLE_CREDENTIALS }}
      #     install_components: "gke-gcloud-auth-plugin"
      #     export_default_credentials: true

      # - name: build and push the docker image
      #   # env:
      #   #   GOOGLE_PROJECT: ${{ secrets.GOOGLE_CREDENTIALS }}
      #   run: |
      #     gcloud auth configure-docker us-central1-docker.pkg.dev
      #     gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://us-central1-docker.pkg.dev
      #     docker build -t us-central1-docker.pkg.dev/inlaid-goods-451523-i3/poc-api/poc-api:latest .
      #     docker push  us-central1-docker.pkg.dev/inlaid-goods-451523-i3/poc-api/poc-api:latest
      #docker build -t poc-api-docker .
      #gcloud auth activate-service-account 850818640270-compute@developer.gserviceaccount.com --key-file=${{ secrets.GOOGLE_CREDENTIALS }}