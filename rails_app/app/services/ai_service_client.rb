require 'httparty'

class AiServiceClient
  include HTTParty
  base_uri ENV.fetch('AI_SERVICE_URL', 'http://localhost:8000')

  def self.analyze(question:, shop_domain:, access_token:)
    new.analyze(question, shop_domain, access_token)
  end

  def analyze(question, shop_domain, access_token)
    response = self.class.post('/analyze', body: {
      query: question,
      shop_domain: shop_domain,
      access_token: access_token
    }.to_json, headers: { 'Content-Type' => 'application/json' })

    if response.success?
      OpenStruct.new(success?: true, body: response.parsed_response)
    else
      OpenStruct.new(success?: false, error_message: response.message)
    end
  rescue StandardError => e
    OpenStruct.new(success?: false, error_message: e.message)
  end
end
