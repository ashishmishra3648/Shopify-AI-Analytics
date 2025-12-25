module Api
  module V1
    class QueriesController < ApplicationController
      include ShopifyApp::EnsureHasSession

      skip_before_action :verify_authenticity_token

      def create
        question = params[:query]
        
        # In a real app, ShopifyApp::EnsureHasSession ensures we have a session.
        # We extract the domain and token from the current session.
        shop_domain = ShopifyAPI::Context.active_session&.shop
        access_token = ShopifyAPI::Context.active_session&.access_token

        # Fallback for demo/testing without real session
        shop_domain ||= "test-store.myshopify.com"
        access_token ||= "shpat_mock_token_12345"

        if question.blank?
          render json: { error: "Question cannot be empty" }, status: :unprocessable_entity
          return
        end

        # Call Python AI Service
        result = AiServiceClient.analyze(
          question: question,
          shop_domain: shop_domain,
          access_token: access_token
        )

        if result.success?
          render json: result.body, status: :ok
        else
          render json: { error: "AI Service failed: #{result.error_message}" }, status: :bad_gateway
        end
      end
    end
  end
end
